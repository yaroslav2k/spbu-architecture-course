import os.path
import re
import io

from dataclasses import dataclass

from abc import ABC, abstractmethod
from pybash.environment import Environment
from pybash.custom_exceptions import UserExitException


environment = Environment()


@dataclass
class CommandStreams:
    output: io.TextIOWrapper
    error: io.TextIOWrapper


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


class EchoCommand(Command):
    """Class that represents echo command."""

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        streams.output.write(" ".join(arguments) + "\n")

        return Command.EXIT_SUCCESS


class CatCommand(Command):
    """Class that represents cat command."""

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        exit_code = Command.EXIT_SUCCESS

        for file_path in arguments:
            if not os.path.exists(file_path):
                streams.output.write(f"cat: {file_path}: No such file or directory\n")
                exit_code = 1
            else:
                with open(file_path) as f:
                    streams.output.write(f.read())

        return exit_code


class WcCommand(Command):
    """Class that represents wc command."""

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        output = ""
        newlines_count, words_count, bytes_count = [], [], []

        exit_code = Command.EXIT_SUCCESS

        for file_path in arguments:
            if os.path.exists(file_path):
                file_content = None
                with open(file_path) as f:
                    file_content = f.read()
                newlines_count.append(file_content.count("\n"))
                file_content = " ".join(file_content.splitlines())
                words_count.append(len(re.split("\s+", file_content)))
                bytes_count.append(os.path.getsize(file_path))
                streams.output.write(
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
                streams.output.write(f"wc: {file_path}: No such file or directory\n")
                exit_code = 1

        if len(arguments) >= 2:
            streams.output.write(
                str(sum(newlines_count))
                + " "
                + str(sum(words_count))
                + " "
                + str(sum(bytes_count))
                + " "
                + "total\n"
            )

        return exit_code


class ExternalCommand(Command):
    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        # TODO: Implement.

        streams.output.write(
            f"Exucuting external command with arguments {arguments}\n",
        )

        return Command.EXIT_SUCCESS


class PwdCommand(Command):
    """Class that represents pwd command."""

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        streams.output.write(environment.get("CURRENT_WORKING_DIRECTORY") + "\n")

        return EXIT_SUCCESS


class AssignCommand(Command):
    """Class that represents variable assignment command."""

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        environment.set(arguments[0], arguments[1])

        return Command.EXIT_SUCCESS


class ExitCommand(Command):
    """Class that represents exit command."""

    def run(self, arguments: list[str], streams: CommandStreams):
        raise UserExitException()
