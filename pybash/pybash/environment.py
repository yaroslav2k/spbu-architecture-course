from __future__ import annotations
from collections.abc import Iterable
import os


class Environment(object):
    """Singleton environment."""

    _instance = None

    @classmethod
    def __new__(cls, *args) -> Environment:
        cls.setup_instance()

        return cls._instance

    @classmethod
    def copy(cls) -> Environment:
        """
        Creates an instance of Environment with the same set of variables.

        Parameters
        ----------
        cls: type
            class to instantiate

        Returns
        -------
        Environment:
            copy of singleton environment
        """
        cls.setup_instance()

        instance = object.__new__(cls)
        instance._variables = dict(cls._instance._variables)

        return instance

    @classmethod
    def setup_instance(cls) -> None:
        """
        Setups signleton environment.

        Parameters
        ----------
        cls: type
            class to instantiate
        """
        if cls._instance is not None:
            return

        cls._instance = object.__new__(cls)
        cls._instance._variables = dict(os.environ)

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
    def items(self) -> Iterable:
        """
        Method to provide dict-like functionality.

        Returns
        -------
        Iterable:
            iterable object
        """
        return iter(self._variables.items())
