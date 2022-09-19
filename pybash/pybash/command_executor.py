from command import EchoCommand, CatCommand

class CommandExecutor:
    def __init__(self, input_stream, output_stream, error_stream):
        self._str2command = {}
        self._str2command["echo"] = EchoCommand("echo")
        self._str2command["cat"] = CatCommand("cat")

        self._input_stream = input_stream
        self._output_stream = output_stream
        self._error_stream = error_stream

    def execute(self, command: str, arguments: list[str]) -> int:
        if command in self._str2command:
            output, exit_status  = self._str2command[command].run(arguments)

        self._output_stream.write(output)
        self._error_stream.write(str(exit_status))

        return 0