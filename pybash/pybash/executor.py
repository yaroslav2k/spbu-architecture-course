import sys

from pybash.parser import Parser, ParsingResult
from pybash.command_executor import CommandExecutor
from pybash.custom_exceptions import UserExitException


class Executor:
    def call(self, string) -> int:
        """
        Executes given user input.

        Parameters
        ----------
        string: str
            string to parse and execute

        Returns
        -------
        int
            command exit code
        """
        if (parsing_result := Parser().parse(string)) is None:
            return

        return CommandExecutor(sys.stdin, sys.stdout, sys.stderr).execute(
            parsing_result.command, parsing_result.arguments
        )
