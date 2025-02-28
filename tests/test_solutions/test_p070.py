from solutions.p070 import get_min_phi_ratio_perm


def test_get_min_phi_ratio_perm() -> None:
    assert get_min_phi_ratio_perm(10**7) == 8319823
