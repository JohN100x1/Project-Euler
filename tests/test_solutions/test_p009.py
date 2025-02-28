from solutions.p009 import get_pytriple_prod


def test_get_pytriple_prod() -> None:
    assert get_pytriple_prod(1000) == 31875000
