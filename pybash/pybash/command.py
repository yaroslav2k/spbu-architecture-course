import os.path
import re

from abc import ABC, abstractmethod
from pybash.environment import Environment


environment = Environment()


class Command(ABC):
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
        }
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


class WcCommand(Command):
    """Class that represents wc command."""

    def run(self, arguments: list[str]) -> tuple[str, int]:
        output = ""
        newlines_count = []
        words_count = []
        bytes_count = []
        exit_status = Command.EXIT_SUCCESS
        for file_path in arguments:
            if os.path.exists(file_path):
                file_content = None
                with open(file_path) as f:
                    file_content = f.read()
                newlines_count.append(file_content.count("\n"))
                file_content = " ".join(file_content.splitlines())
                words_count.append(len(re.split("\s+", file_content)))
                bytes_count.append(os.path.getsize(file_path))
                output += (
                    str(newlines_count[-1])
                    + "  "
                    + str(words_count[-1])
                    + " "
                    + str(bytes_count[-1])
                    + " "
                    + str(file_path)
                    + "\n"
                )
            else:
                output += f"wc: {file_path}: No such file or directory\n"
                exit_status = 1

        if len(arguments) >= 2:
            output += (
                str(sum(newlines_count))
                + " "
                + str(sum(words_count))
                + " "
                + str(sum(bytes_count))
                + " "
                + "total\n"
            )

        return output, exit_status


class ExternalCommand(Command):
    def run(self, arguments: list[str]) -> tuple[str, int]:
        # TODO: Implement.
        return (
            f"Exucuting external command with arguments {arguments}\n",
            Command.EXIT_SUCCESS,
        )


class PwdCommand(Command):
    """Class that represents pwd command."""

    def run(self, arguments: list[str]) -> tuple[str, str]:
        cwd = environment.get("CURRENT_WORKING_DIRECTORY") + "\n"
        return (cwd, Command.EXIT_SUCCESS)


class AssignCommand(Command):
    """Class that represents variable assignment command."""

    def run(self, arguments: list[str]) -> tuple[str, int]:
        environment.set(arguments[0], arguments[1])
        return ("", Command.EXIT_SUCCESS)
