from config import NUMERAL_CHR, NUMERAL_VAL, path_res


def load_numerals() -> list[str]:
    """Load a list of roman numerals from /res/p089_roman.txt"""
    with open(path_res / "p089_roman.txt") as f:
        return f.read().split("\n")


def get_roman_numeral(n: int) -> str:
    """Get the Roman numeral of a number n."""
    int_string = str(n)[::-1]
    numeral = ""
    for i in range(min(len(int_string), 3)):
        multiple = int(int_string[i])
        if multiple == 0:
            continue
        unit = NUMERAL_CHR[10**i]
        half = NUMERAL_CHR[5 * 10**i]
        full = NUMERAL_CHR[10 ** (i + 1)]
        if multiple % 4 == 0 and multiple % 8 != 0:
            numeral += half + unit
        elif multiple % 9 == 0:
            numeral += full + unit
        else:
            numeral += unit * (multiple % 5) + half * (multiple // 5)

    numeral += "M" * (n // 1000)
    return numeral[::-1]


def get_number_from_numeral(numeral: str) -> int:
    """Get the number represented by the Roman numeral."""
    num = 0
    increment = 1
    last_symbol = "I"
    for i, symbol in enumerate(reversed(numeral)):
        value = NUMERAL_VAL[symbol]
        if value >= increment:
            increment = value
            num += value
        elif symbol == "I" and last_symbol in {"V", "X"}:
            num -= 1
        elif symbol == "X" and last_symbol in {"L", "C"}:
            num -= 10
        elif symbol == "C" and last_symbol in {"D", "M"}:
            num -= 100
        last_symbol = symbol
    return num


def count_numerals_saved(numerals: list[str]) -> int:
    """
    Get the number of numerals saved by converting a list of Roman numerals
    to their minimal form.
    """
    num_saved = 0
    for numeral in numerals:
        num = get_number_from_numeral(numeral)
        min_numeral = get_roman_numeral(num)
        num_saved += len(numeral) - len(min_numeral)
    return num_saved
