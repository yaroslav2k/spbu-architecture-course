from pybash.command import Command, CommandStreams
from pybash.custom_exceptions import UserExitException


class CommandExecutor:
    def __init__(self, input_stream, output_stream, error_stream):
        self._input_stream = input_stream
        self._output_stream = output_stream
        self._error_stream = error_stream

    def execute(self, command: str, arguments: list[str]) -> int:
        command = Command.build(command)
        command_streams = CommandStreams(self._output_stream, self._error_stream)

        exit_code = command.run(arguments, command_streams)

        return exit_code
