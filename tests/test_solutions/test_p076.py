from solutions.p076 import count_partitions


def test_count_partitions() -> None:
    assert count_partitions(100) == 190569291
