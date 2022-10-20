import os
from pathlib import Path
import re
from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams
from pybash.environment import Environment


class WcCommand(BaseCommand):
    """Class that represents wc command."""

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        newlines_count, words_count, bytes_count = [], [], []

        exit_code = BaseCommand.EXIT_SUCCESS

        cur_path = Path(Environment().get('PWD'))
        for file_path in arguments:
            full_file_path = cur_path / file_path
            if not full_file_path.exists():
                streams.output.write(f"wc: {file_path}: No such file or directory\n")
                exit_code = 1
            elif not os.access(full_file_path, os.R_OK):
                streams.output.write(f"wc: {file_path}: Permission denied\n")
                exit_code = 1
            elif full_file_path.is_dir():
                streams.output.write(f"wc: {file_path}: Is a directory\n")
                streams.output.write(f"0 0 0 {file_path}\n")
                exit_code = 1
            else:
                file_content = None
                with open(full_file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                newlines_count.append(file_content.count("\n"))
                file_content = " ".join(file_content.splitlines())
                words_count.append(len(re.split(r"\s+", file_content)))
                bytes_count.append(os.path.getsize(full_file_path))
                if bytes_count[-1] == 0:
                    words_count[-1] = 0
                streams.output.write(
                    str(newlines_count[-1])
                    + " "
                    + str(words_count[-1])
                    + " "
                    + str(bytes_count[-1])
                    + " "
                    + str(file_path)
                    + "\n"
                )

        if len(arguments) >= 2:
            streams.output.write(
                str(sum(newlines_count))
                + " "
                + str(sum(words_count))
                + " "
                + str(sum(bytes_count))
                + " "
                + "total\n"
            )

        return exit_code
