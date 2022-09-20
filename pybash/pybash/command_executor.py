from pybash.command import Command


class CommandExecutor:
    def __init__(self, input_stream, output_stream, error_stream):
        self._input_stream = input_stream
        self._output_stream = output_stream
        self._error_stream = error_stream

    def execute(self, command: str, arguments: list[str]) -> int:
        command = Command.build(command, arguments)
        output, exit_code = command.run()

        self._output_stream.write(output)
        if exit_code > 0:
            self._error_stream.write(str(exit_code))

        return 0
