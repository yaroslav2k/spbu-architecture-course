import subprocess
import sys
import platform

from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams
from pybash.custom_exceptions import UnknownCommandException
from pybash.environment import Environment


class ExternalCommand(BaseCommand):
    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        try:
            completed_process = subprocess.run(
                arguments,
                stdin=streams.input,
                stdout=streams.output,
                stderr=streams.error,
                env=Environment().get_variables(),
            )
        except FileNotFoundError:
            raise UnknownCommandException(arguments[0])

        return completed_process.returncode

    def is_external(self) -> bool:
        return True
