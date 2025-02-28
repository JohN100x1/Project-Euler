from solutions.p002 import sum_even_fib


def test_sum_even_fib() -> None:
    assert sum_even_fib(4000000) == 4613732
