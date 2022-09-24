from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams


class ExternalCommand(BaseCommand):
    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        # TODO: Implement.

        streams.output.write(
            f"Exucuting external command with arguments {arguments}\n",
        )

        return BaseCommand.EXIT_SUCCESS
