import re

from pybash.environment import Environment


class SubstitutionProcessor:
    """Class that makes substitutions from environment variables."""

    def __init__(self):
        pass

    def substitute(self, user_input: str) -> str:
        """
        Substitutes all occurrences of $var_name with respect to full and weak quoting.

        Parameters
        ----------
        user_input: str
            string in which substitutions should be made

        Returns
        -------
        str
            string after all substitutions
        """
        substituted_input = re.sub(
            r"'.*'|\".*\"|\$[^.,!?\s\\\/\$]+|\$",
            self._match_substution,
            user_input,
        )
        return substituted_input

    def _match_substution(self, match: re.Match[str]) -> str:
        match_str = match.group()
        if match_str[0] == '"':
            return re.sub(
                r"\$[^.,!?\s\\\/\$\"\']+",
                lambda m: Environment().get(m.group()[1:]),
                match_str,
            )
        elif match_str[0] == "'":
            return match_str
        elif match_str == "$":
            return "$"
        else:
            return Environment().get(match_str[1:])
