from abc import ABC, abstractmethod

from pybash.commands.command_streams import CommandStreams


class BaseCommand(ABC):
    """Abstract class that represents a command."""

    EXIT_SUCCESS = 0

    def __init__(self):
        pass

    @staticmethod
    def build(command: str):
        mapping = {
            "echo": EchoCommand,
            "cat": CatCommand,
            "assign": AssignCommand,
            "wc": WcCommand,
            "pwd": PwdCommand,
            "exit": ExitCommand,
        }

        return mapping.get(command, ExternalCommand)()

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
