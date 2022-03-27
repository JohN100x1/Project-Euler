from pathlib import Path

from utils.primes import get_primes

# Path to source code and resources
path_root = Path(__file__).parent.parent
path_res = path_root / "res"
path_src = path_root / "src"
path_tests = path_root / "tests"

# Determine the number of primes used.
# This will affect certain utility functions which use primes.
PRIMES = get_primes(10**6)
PRIME_SET = set(PRIMES)

# A useful set of digits
DIGITS = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
NON_ZERO_DIGITS = {1, 2, 3, 4, 5, 6, 7, 8, 9}
