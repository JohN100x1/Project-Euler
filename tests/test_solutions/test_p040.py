from solutions.p040 import prod_nth_champernowne


def test_prod_nth_champernowne():
    assert prod_nth_champernowne([10**k for k in range(1, 7)]) == 210
