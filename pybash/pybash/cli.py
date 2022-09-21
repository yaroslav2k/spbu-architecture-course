from pybash.executor import Executor
from pybash.custom_exceptions import UserExitException


class CLI:
    def __init__(self):
        self.executor = Executor()

    def run(self) -> None:
        while True:
            user_input = input(">: ")

            try:
                self.executor.call(user_input)
            except UserExitException:
                break


if __name__ == "__main__":
    cli = CLI()
    cli.run()
