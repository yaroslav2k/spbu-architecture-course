import os.path

from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract class that represents a command."""
    EXIT_SUCCESS = 0

    def __init__(self):
        pass

    @staticmethod
    def build(command: str):
        mapping = {"echo": EchoCommand, "cat": CatCommand, "assign": AssignCommand}
        handler = mapping.get(command, ExternalCommand)

        return handler()

    @abstractmethod
    def run(self, arguments: list[str]) -> tuple[str, int]:
        """
        Runs the command with given list of arguments.

        Parameters
        ----------
        arguments: list[str]
            arguments of a command
        
        Returns
        -------
        tuple[str, int]
            command output and exit status
        """
        pass


class EchoCommand(Command):
    """Class that represents echo command."""
    def run(self, arguments: list[str]) -> tuple[str, int]:
        return " ".join(arguments) + "\n", Command.EXIT_SUCCESS


class CatCommand(Command):
    """Class that represents cat command."""
    def run(self, arguments: list[str]) -> tuple[str, int]:
        output = ""
        exit_status = Command.EXIT_SUCCESS
        for file_path in arguments:
            if not os.path.exists(file_path):
                output += f"cat: {file_path}: No such file or directory\n"
                exit_status = 1
            else:
                with open(file_path) as f:
                    output += f.read()

        return output, exit_status


class ExternalCommand(Command):
    def run(self, arguments: list[str]) -> tuple[str, int]:
        # TODO: Implement.
        return (
            f"Exucuting external command with arguments {arguments}\n",
            Command.EXIT_SUCCESS,
        )


class AssignCommand(Command):
    def run(self, arguments: list[str]) -> tuple[str, int]:
        # TODO: Implement.
        return (
            f"Exucuting assign command with arguments {arguments}\n",
            Command.EXIT_SUCCESS,
        )
