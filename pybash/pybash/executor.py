import sys

from pybash.parser import Parser
from pybash.command_executor import CommandExecutor
from pybash.custom_exceptions import UserExitException


class Executor:
    def call(self, string):
        command, arguments = Parser().parse(string)

        try:
            CommandExecutor(sys.stdin, sys.stdout, sys.stderr).execute(
                command, arguments
            )
        except UserExitException:
            raise
