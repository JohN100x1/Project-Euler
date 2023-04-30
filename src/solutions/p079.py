from collections import defaultdict

from requests import get

from utils.exceptions import SolutionNotFoundError


class KeyLog(tuple):
    pass


def load_logins() -> list[KeyLog]:
    """Load a list of integer tuples from p079_keylog.txt"""
    url = "https://projecteuler.net/project/resources/p079_keylog.txt"
    content = get(url).content.decode("utf-8").rstrip("\n")
    return [KeyLog(int(d) for d in n) for n in content.split("\n")]


class PasscodeSearch:
    """Search for passcode using DFS."""

    def __init__(self):
        self.passcodes = []
        self.right_adj: dict[int, set[int]] = {}

    def dfs_traverse(self, passcode: int, d: int):
        """Search for Passcode using DFS."""
        if d not in self.right_adj:
            self.passcodes.append(passcode)
            return
        for next_d in self.right_adj[d]:
            self.dfs_traverse(passcode * 10 + next_d, next_d)

    @staticmethod
    def generate_right_adj(logins: list[KeyLog]) -> dict[int, set[int]]:
        """Generate the Right adjacent digits of the passcodes from logins."""
        right_adj = defaultdict(set)
        # Initial right adjacent digits
        for keylog in logins:
            for idx in range(len(keylog) - 1):
                right_adj[keylog[idx]].add(keylog[idx + 1])
            # The third digit cannot be adjacent to the first digit
            # Sets are used assuming passcode digits appear at most once.
            if keylog[2] in right_adj[keylog[0]]:
                right_adj[keylog[0]].remove(keylog[2])
        return right_adj

    def generate_short_passcode(self, logins: list[KeyLog]) -> int:
        """Return the shortest passcode from a given list of keyed logins."""
        self.passcodes = []
        self.right_adj = self.generate_right_adj(logins)
        # Get the first digit
        has_next_digits = set(d for d in self.right_adj.keys())
        next_digits = set(d for dset in self.right_adj.values() for d in dset)
        start_digit = [d for d in has_next_digits if d not in next_digits]
        # Traverse graph to get passcodes
        self.dfs_traverse(start_digit[0], start_digit[0])
        # Check passcode contains all digits; return first instance
        dset = has_next_digits | next_digits
        for passcode in self.passcodes:
            if set(int(d) for d in str(passcode)) == dset:
                return passcode
        raise SolutionNotFoundError("Failed to find passcode.")
