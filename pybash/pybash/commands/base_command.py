from abc import ABC, abstractmethod

from pybash.commands.command_streams import CommandStreams


class BaseCommand(ABC):
    """Abstract class that represents a command."""

    EXIT_SUCCESS = 0

    def __init__(self):
        pass

    @abstractmethod
    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        """
        Runs the command with given list of arguments.

        Parameters
        ----------
        arguments: list[str]
            arguments of a command

        streams: CommandStreams
            streams

        Returns
        -------
        int
            command exit code
        """
        pass

    def is_external(self) -> bool:
        """
        Checking if a command is external or built-in.

        Returns
        -------
        bool
            True if a command is external, False otherwise
        """
        return False
