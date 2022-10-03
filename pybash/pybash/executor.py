import sys
from tempfile import TemporaryFile

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
        # NOTE: Current implementation uses temporary files which does not seem to be
        # a good approach in terms of performance. However, it seems to be an appropriate solution
        # for POC (and in case of relatively small tmp-file contents it might be buffered in OS cache to prevent
        # redundant disk IO operations).
        if (parsing_result := Parser().parse(string)) is None:
            return

        exit_code = None
        input_stream, output_stream = sys.stdin, self._create_stream()
        commands_count = len(parsing_result.commands)

        for index, command in enumerate(parsing_result.commands):
            if is_last_command := index == commands_count - 1:
                output_stream = sys.stdout

            exit_code = CommandExecutor(
                input_stream, output_stream, sys.stderr
            ).execute(command[0], command[1])

            input_stream, output_stream = output_stream, self._create_stream()
            if not is_last_command:
                input_stream.seek(0)

        return exit_code

    @staticmethod
    def _create_stream():
        return TemporaryFile(mode="w+")
