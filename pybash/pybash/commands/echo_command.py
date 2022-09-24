from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams


class EchoCommand(BaseCommand):
    """Class that represents echo command."""

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        streams.output.write(" ".join(arguments) + "\n")

        return BaseCommand.EXIT_SUCCESS
