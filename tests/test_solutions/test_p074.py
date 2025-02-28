from solutions.p074 import count_chains_with_length


def test_count_chains_with_length() -> None:
    assert count_chains_with_length(60, 10**6) == 402
