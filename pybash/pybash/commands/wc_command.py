from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams


class WcCommand(BaseCommand):
    """Class that represents wc command."""

    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        output = ""
        newlines_count, words_count, bytes_count = [], [], []

        exit_code = BaseCommand.EXIT_SUCCESS

        for file_path in arguments:
            if os.path.exists(file_path):
                file_content = None
                with open(file_path) as f:
                    file_content = f.read()
                newlines_count.append(file_content.count("\n"))
                file_content = " ".join(file_content.splitlines())
                words_count.append(len(re.split("\s+", file_content)))
                bytes_count.append(os.path.getsize(file_path))
                streams.output.write(
                    str(newlines_count[-1])
                    + "  "
                    + str(words_count[-1])
                    + " "
                    + str(bytes_count[-1])
                    + " "
                    + str(file_path)
                    + "\n"
                )
            else:
                streams.output.write(f"wc: {file_path}: No such file or directory\n")
                exit_code = 1

        if len(arguments) >= 2:
            streams.output.write(
                str(sum(newlines_count))
                + " "
                + str(sum(words_count))
                + " "
                + str(sum(bytes_count))
                + " "
                + "total\n"
            )

        return exit_code
