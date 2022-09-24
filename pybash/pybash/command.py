from pybash.commands import *


class Command:
    @staticmethod
    def build(command: str) -> BaseCommand:
        mapping = {
            "echo": EchoCommand,
            "cat": CatCommand,
            "assign": AssignCommand,
            "wc": WcCommand,
            "pwd": PwdCommand,
            "exit": ExitCommand,
        }

        return mapping.get(command, ExternalCommand)()
