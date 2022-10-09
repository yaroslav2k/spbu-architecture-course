import argparse
from dataclasses import dataclass
import re
import os

from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams
from pybash.custom_exceptions import InvalidArgumentException


class GrepCommand(BaseCommand):
    """Class that represents grep command."""

    class _ArgumentsParser:
        @dataclass
        class Result:
            word_regexp: bool
            ignore_case: bool
            after_context: int
            search: str
            files: list[str]

        def __init__(self):
            self._parser = self._build_parser()

        def parse(self, value: str) -> Result:
            arguments, files = None, None
            try:
                arguments, files = self._parser.parse_known_args(value)
            except argparse.ArgumentError as e:
                raise InvalidArgumentException(str(e))

            files = files or []

            return self.Result(
                word_regexp=arguments.word_regexp,
                ignore_case=arguments.ignore_case,
                after_context=arguments.after_context,
                search=files[0] if len(files) else None,
                files=files[1:],
            )

        def _build_parser(self) -> argparse.ArgumentParser:
            parser = argparse.ArgumentParser(add_help=False, exit_on_error=False)
            parser.add_argument("-w", "--word-regexp", action="store_true")
            parser.add_argument("-i", "--ignore-case", action="store_true")
            parser.add_argument("-A", "--after-context", type=int)

            return parser

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        parsed_arguments = self._ArgumentsParser().parse(arguments)
        self._validate_arguments(parsed_arguments)

        pattern = parsed_arguments.search
        if parsed_arguments.word_regexp:
            pattern = r"\b" + pattern + r"\b"

        pattern_compiled = None
        if parsed_arguments.ignore_case:
            pattern_compiled = re.compile(pattern, re.IGNORECASE)
        else:
            pattern_compiled = re.compile(pattern)

        exit_code = 1
        num_paragraphs = 0
        for file_path in parsed_arguments.files:
            if not os.path.exists(file_path):
                streams.output.write(f"grep: {file_path}: No such file or directory\n")
                exit_code = 2
                continue
            elif os.path.isdir(file_path):
                streams.output.write(f"grep: {file_path}: Is a directory\n")
                exit_code = 2
                continue
            inside_paragraph = False
            with open(file_path, "r") as file:
                last_match_line = None
                for idx, line in enumerate(file):
                    match = pattern_compiled.search(line)
                    if match:
                        if exit_code != 2:
                            exit_code = BaseCommand.EXIT_SUCCESS
                        if num_paragraphs > 0 and not inside_paragraph:
                            streams.output.write("--\n")
                        inside_paragraph = True
                        output = line
                        if output[-1] != "\n":
                            output += "\n"
                        if len(parsed_arguments.files) > 1:
                            output = file_path + ":" + output

                        last_match_line = idx
                        streams.output.write(output)
                    elif None not in (last_match_line, parsed_arguments.after_context):
                        if idx - last_match_line <= parsed_arguments.after_context:
                            output = line
                            if output[-1] != "\n":
                                output += "\n"
                            if len(parsed_arguments.files) > 1:
                                output = file_path + ":" + output
                            streams.output.write(output)
                        elif (
                            idx - last_match_line == parsed_arguments.after_context + 1
                        ):
                            num_paragraphs += 1
                            inside_paragraph = False
                if None not in (last_match_line, parsed_arguments.after_context):
                    num_paragraphs += 1

        return exit_code

    def _validate_arguments(self, arguments: _ArgumentsParser.Result) -> None:
        if arguments.search is None or not len(arguments.files):
            raise InvalidArgumentException(
                "error: provide a string to search and file(s) to search in"
            )
