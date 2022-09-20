from pybash.executor import Executor


class CLI:
    def __init__(self):
        self.executor = Executor()

    def run(self) -> None:
        while True:
            user_input = input(">: ")

            if user_input == "exit":
                break

            self.executor.call(user_input)


if __name__ == "__main__":
    cli = CLI()
    cli.run()
