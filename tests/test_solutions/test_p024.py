from solutions.p024 import get_nth_lexicographic_perm


def test_get_nth_lexicographic_perm():
    dlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert get_nth_lexicographic_perm(dlist, 1000000) == 2783915460
