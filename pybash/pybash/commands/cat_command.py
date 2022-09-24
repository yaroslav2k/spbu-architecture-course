import os

from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams


class CatCommand(BaseCommand):
    """Class that represents cat command."""

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        exit_code = BaseCommand.EXIT_SUCCESS

        for file_path in arguments:
            if not os.path.exists(file_path):
                streams.output.write(f"cat: {file_path}: No such file or directory\n")
                exit_code = 1
            elif os.path.isdir(file_path):
                streams.output.write(f"cat: {file_path}: Is a directory\n")
                exit_code = 1
            else:
                with open(file_path) as f:
                    streams.output.write(f.read())

        return exit_code
