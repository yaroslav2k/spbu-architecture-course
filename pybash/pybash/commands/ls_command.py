import os
from pathlib import Path
from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams
from pybash.custom_exceptions import InvalidArgumentException
from pybash.environment import Environment


class LsCommand(BaseCommand):
    """Class that represents ls command."""

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        if len(arguments) > 1:
            streams.output.write("Too many arguments for ls-command\n")
            return -1

        path = Path(Environment().get("PWD"))            
        if len(arguments) == 1:
            path = path / arguments[0]
        if not path.exists():
            streams.output.write("Path doesn't exist\n")
            return -1

        streams.output.write('\n'.join(os.listdir(path)) + '\n')
        return BaseCommand.EXIT_SUCCESS
