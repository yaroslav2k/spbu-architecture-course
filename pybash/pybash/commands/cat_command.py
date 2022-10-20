import os
from pathlib import Path
from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams
from pybash.environment import Environment


class CatCommand(BaseCommand):
    """Class that represents cat command."""

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        exit_code = BaseCommand.EXIT_SUCCESS

        cur_path = Path(Environment().get("PWD"))
        for file_path in arguments:
            full_file_path = cur_path / file_path
            if not full_file_path.exists():
                streams.output.write(f"cat: {file_path}: No such file or directory\n")
                exit_code = 1
            elif not os.access(full_file_path, os.R_OK):
                streams.output.write(f"cat: {file_path}: Permission denied\n")
                exit_code = 1
            elif full_file_path.is_dir():
                streams.output.write(f"cat: {file_path}: Is a directory\n")
                exit_code = 1
            else:
                with open(full_file_path, 'r', encoding='utf-8') as f:
                    streams.output.write(f.read())

        return exit_code
