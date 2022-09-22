from pybash.command import Command
from pybash.custom_exceptions import UserExitException


class CommandExecutor:
    def __init__(self, input_stream, output_stream, error_stream):
        self._input_stream = input_stream
        self._output_stream = output_stream
        self._error_stream = error_stream

    def execute(self, command: str, arguments: list[str]) -> int:
        command = Command.build(command)

        output, exit_code = command.run(arguments)

        self._output_stream.write(output)
        if exit_code > 0:
            self._error_stream.write(str(exit_code))

        return 0
