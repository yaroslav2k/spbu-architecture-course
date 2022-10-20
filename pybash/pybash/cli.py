from pybash.executor import Executor
from pybash.custom_exceptions import (
    UserExitException,
    ParsingFailureException,
    UnknownCommandException,
    InvalidArgumentException,
)


class CLI:
    _last_exit_code = None

    def __init__(self):
        self._executor = Executor()

    def run(self) -> None:
        """CLI entrypoint."""
        while True:
            user_input = input("$ ")

            try:
                _last_exit_code = self._executor.call(user_input)
            except UserExitException:
                break
            except ParsingFailureException:
                print("Syntax error")
            except UnknownCommandException as e:
                print(f"{e.args[0]}: command not found")
            except InvalidArgumentException as e:
                print(e.args[0])
            except BaseException as e:
                print("Unknown error: ", e)


if __name__ == "__main__":
    CLI().run()
