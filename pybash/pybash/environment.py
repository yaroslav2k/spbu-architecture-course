import os


class Environment(object):
    """Singleton environment."""

    _instance = None

    @classmethod
    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance._variables = dict(os.environ)
        return cls._instance

    @classmethod
    def copy(cls):
        instance = object.__new__(cls)
        instance._variables = dict(cls._instance._variables)

        return instance

    def set(self, key: str, value: str) -> None:
        """
        Sets an environmental variable.

        Parameters
        ----------
        key: str
            name of a variable to be set

        value: str
            value to set
        """
        self._instance._variables[key] = value

    def get(self, key: str) -> str:
        """
        Gets an environmental variable.

        Parameters
        ----------
        key: str
            name of a variable to be returned

        Returns
        -------
        str:
            value of a variable
        """
        return self._instance._variables.get(key, "")

    # TODO: delegate
    def items(self, *args, **kwargs):
        return iter(self._variables.items(*args, **kwargs))
