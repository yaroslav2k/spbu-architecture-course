from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams
from pybash.custom_exceptions import UserExitException


class ExitCommand(BaseCommand):
    """Class that represents exit command."""

    def run(self, arguments: list[str], streams: CommandStreams):
        raise UserExitException()
