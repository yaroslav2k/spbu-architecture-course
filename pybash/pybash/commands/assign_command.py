from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams
from pybash.environment import Environment


class AssignCommand(BaseCommand):
    """Class that represents variable assignment command."""

    _INTERNAL_IDENTIFIER = "__internal_assign"

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        Environment().set(arguments[0], arguments[1])

        return BaseCommand.EXIT_SUCCESS
