from __future__ import annotations
from collections.abc import Iterable
import os


class Environment(object):
    """Singleton environment."""

    _instance = None

    @classmethod
    def __new__(cls, *args) -> Environment:
        cls._setup_instance()

        return cls._instance

    @classmethod
    def _setup_instance(cls) -> None:
        if cls._instance is not None:
            return

        cls._instance = object.__new__(cls)
        cls._instance._variables = dict(os.environ)
        # NOTE: We have to set PWD environment variable explicitly due
        # to WinAPI issues.
        cls._instance._variables["PWD"] = os.getcwd()

    def get_variables(self) -> dict:
        """
        Get stored environment variables.

        Returns
        -------
        dict:
            environment variables
        """
        return self._variables

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
