import argparse
from dataclasses import dataclass

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
            files: list[str]

        def __init__(self):
            parser = argparse.ArgumentParser(add_help=False, exit_on_error=False)
            parser.add_argument("-w", "--word-regexp", action="store_true")
            parser.add_argument("-i", "--ignore-case", action="store_true")
            parser.add_argument("-A", "--after-context", type=int)

            self._parser = parser

        def parse(self, value: str) -> Result:
            arguments, files = None, None
            try:
                arguments, files = self._parser.parse_known_args(value)
            except argparse.ArgumentError as e:
                raise InvalidArgumentException(str(e))

            return self.Result(
                word_regexp=arguments.word_regexp,
                ignore_case=arguments.ignore_case,
                after_context=arguments.after_context,
                files=files,
            )

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        parsed_arguments = self._ArgumentsParser().parse(arguments)

        # TODO: Provide required implementation.
        streams.output.write(f"Invoked grep via {parsed_arguments}\n")

        return BaseCommand.EXIT_SUCCESS
