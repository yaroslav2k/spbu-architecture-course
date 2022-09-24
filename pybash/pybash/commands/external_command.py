import subprocess
import sys

from pybash.commands.base_command import BaseCommand
from pybash.commands.command_streams import CommandStreams
from pybash.environment import Environment


class ExternalCommand(BaseCommand):
    def run(self, arguments: list[str], streams: CommandStreams) -> int:
        completed_process = subprocess.run(
            arguments,
            stdin=streams.input,
            stdout=streams.output,
            stderr=streams.error,
            env=Environment.copy(),
        )

        return completed_process.returncode

    def is_external(self):
        return True
