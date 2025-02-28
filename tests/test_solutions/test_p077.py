from solutions.p077 import get_prime_partition_count_over


def test_get_prime_partition_count_over() -> None:
    assert get_prime_partition_count_over(5000) == 71
