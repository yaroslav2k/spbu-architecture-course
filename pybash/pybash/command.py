from abc import ABC, abstractmethod
import os.path


class Command(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, arguments: list[str]) -> tuple[str, int]:
        '''
        Runs the command with given list of arguments.

        Parameters
        ----------
        arguments: list[str]
            arguments of a command

        Returns
        -------
        tuple[str, int]
            command output and exit status
        '''
        pass


class EchoCommand(Command):
    def run(self, arguments: list[str]) -> tuple[str, int]:
        return " ".join(arguments), 0


class CatCommand(Command):
    def run(self, arguments: list[str]) -> tuple[str, int]:
        output = ""
        for file_path in arguments:
            if not os.path.exists(file_path):
                output += f'cat: {file_path}: No such file or directory'
                return output, 1

            with open(file_path) as f:
                output += f.read()

        return output, 0
