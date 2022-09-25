from pybash.commands import *


class Command:
    @staticmethod
    def build(command: str) -> BaseCommand:
        """
        Builder method to create an instance of specific command class from string.

        Parameters
        ----------
        command: str
            string representation of command

        Returns
        -------
        BaseCommand:
            specific instance of BaseCommand subclass
        """
        mapping = {
            "echo": EchoCommand,
            "cat": CatCommand,
            "assign": AssignCommand,
            "wc": WcCommand,
            "pwd": PwdCommand,
            "exit": ExitCommand,
        }

        return mapping.get(command, ExternalCommand)()
