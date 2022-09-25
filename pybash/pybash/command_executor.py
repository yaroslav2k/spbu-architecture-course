from pybash.command import Command
from pybash.commands.command_streams import CommandStreams


class CommandExecutor:
    def __init__(self, input_stream, output_stream, error_stream):
        self._input_stream = input_stream
        self._output_stream = output_stream
        self._error_stream = error_stream

    def execute(self, command: str, arguments: list[str]) -> int:
        """
        Executes given command with arguments.

        Parameters
        ----------
        command: str
            command to execute

        arguments: list[str]
            list of arguments to execute command with

        Returns
        -------
        int
            command exit code
        """
        command_handler = Command.build(command)
        command_streams = CommandStreams(
            self._input_stream, self._output_stream, self._error_stream
        )

        if command_handler.is_external():
            arguments = [command] + arguments

        return command_handler.run(arguments, command_streams)
