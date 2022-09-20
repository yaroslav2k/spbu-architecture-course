import sys

from pybash.parser import Parser
from pybash.command_executor import CommandExecutor


class Executor:
    def call(self, string):
        command, arguments = Parser().parse(string)

        CommandExecutor(sys.stdin, sys.stdout, sys.stderr).execute(command, arguments)
