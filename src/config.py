from math import factorial
from pathlib import Path

# Path to source code and resources
path_root = Path(__file__).parent.parent
path_res = path_root / "res"
path_src = path_root / "src"
path_tests = path_root / "tests"

# A useful set of digits
DIGITS = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
NON_ZERO_DIGITS = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Digit factorials
DIGIT_FACTORIALS = {str(i): factorial(i) for i in range(10)}

# Fifth powers
DIGIT_FIFTH_POWER = {str(i): i**5 for i in range(10)}

# Roman numerals
NUMERAL_VAL = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
NUMERAL_CHR = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
