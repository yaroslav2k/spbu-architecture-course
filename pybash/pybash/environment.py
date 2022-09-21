import os


class Environment(object):
    """Singleton environment."""

    obj = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.obj._variables = {"CURRENT_WORKING_DIRECTORY": os.getcwd()}
        return cls.obj

    def set(self, variable: str, value: str) -> None:
        """
        Sets an environmental variable.

        Parameters
        ----------
        variable: str
            name of a variable to be set

        value: str
            value to set
        """
        self.obj._variables[variable] = value

    def get(self, variable: str) -> str:
        """
        Gets an environmental variable.

        Parameters
        ----------
        variable: str
            name of a variable to be returned

        Returns
        -------
        str:
            value of a variable
        """
        return self.obj._variables[variable]
