from solutions.p015 import count_lattice_paths


def test_get_lattice_paths() -> None:
    assert count_lattice_paths(20) == 137846528820
