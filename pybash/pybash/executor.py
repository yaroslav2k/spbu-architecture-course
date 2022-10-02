import sys

from pybash.parser import Parser, ParsingResult
from pybash.command_executor import CommandExecutor


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

        # TODO: Implement commands piping.
        exit_code = None
        for command in parsing_result.commands:
            exit_code = CommandExecutor(sys.stdin, sys.stdout, sys.stderr).execute(
                command[0], command[1]
            )

        return exit_code
