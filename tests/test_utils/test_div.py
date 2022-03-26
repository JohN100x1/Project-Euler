import pytest

from utils.div import (
    get_num_divisors,
    get_prime_factorisation,
    sum_factors,
    sum_proper_factors,
)


class TestGetNumDivisors:
    """Test get_num_divisors."""

    def test_integer_greater_than_one(self):
        assert get_num_divisors(45) == 6

    def test_one_divisor(self):
        assert get_num_divisors(1) == 1

    def test_error(self):
        with pytest.raises(ValueError, match="out of range. Choose n > 0."):
            assert get_num_divisors(0)


class TestGetPrimeFactorisation:
    """Test get_prime_factorisation."""

    def test_integer_greater_than_one(self):
        assert get_prime_factorisation(180) == {2: 2, 3: 2, 5: 1}

    def test_no_prime_factors(self):
        assert get_prime_factorisation(1) == {}

    def test_error(self):
        with pytest.raises(ValueError, match="out of range. Choose n > 0."):
            assert get_prime_factorisation(0)


class TestSumFactors:
    """Test sum_factors."""

    def test_integer_greater_than_one(self):
        assert sum_factors(192) == 508

    def test_one(self):
        assert sum_factors(1) == 1

    def test_error(self):
        with pytest.raises(ValueError, match="out of range. Choose n > 0."):
            assert sum_factors(0)


class TestSumProperFactors:
    """Test sum_proper_factors."""

    def test_integer_greater_than_one(self):
        assert sum_proper_factors(192) == 316

    def test_one(self):
        assert sum_proper_factors(1) == 0

    def test_error(self):
        with pytest.raises(ValueError, match="out of range. Choose n > 0."):
            assert sum_proper_factors(0)
