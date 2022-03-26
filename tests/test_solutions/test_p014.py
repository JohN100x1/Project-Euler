from solutions.p014 import get_longest_collatz_seq


def test_get_longest_collatz_seq():
    assert get_longest_collatz_seq(1000000) == 837799
