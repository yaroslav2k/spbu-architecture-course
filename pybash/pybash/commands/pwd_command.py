from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams
from pybash.environment import Environment


class PwdCommand(BaseCommand):
    """Class that represents pwd command."""

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        streams.output.write(Environment().get("PWD") + "\n")

        return BaseCommand.EXIT_SUCCESS
