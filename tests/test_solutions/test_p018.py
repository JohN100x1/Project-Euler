from solutions.p018 import get_max_path, load_paths


def test_get_max_paths() -> None:
    paths = load_paths()
    assert get_max_path(paths) == 1074
