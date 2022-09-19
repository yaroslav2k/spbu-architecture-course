from abc import ABC, abstractmethod
import os.path


class Command(ABC):
    def __init__(self, arguments: list[str]):
        self.arguments = arguments

    @staticmethod
    def build(command: str, arguments: list[str]):
        match str(command):
            case "echo":
                return EchoCommand(arguments)
            case "cat":
                return CatCommand(arguments)
            case _:
                pass  # FIXME: Handle via some sort of ExternalCommand.

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
    def run(self, arguments: list[str]) -> tuple[str, int]:
        return " ".join(arguments), 0


class CatCommand(Command):
    def run(self, arguments: list[str]) -> tuple[str, int]:
        output = ""
        exit_status = 0
        for file_path in arguments:
            if not os.path.exists(file_path):
                output += f"cat: {file_path}: No such file or directory\n"
                exit_status = 1
            else:
                with open(file_path) as f:
                    output += f.read()

        return output, exit_status
