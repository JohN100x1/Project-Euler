from collections import defaultdict
from typing import Generator

from utils.primes import get_primes, miller_rabin_is_prime


def is_pair(p: int, q: int) -> bool:
    """Return boolean of whether p and q concatenate to form a prime."""
    p_string, q_string = str(p), str(q)
    num1, num2 = int(p_string + q_string), int(q_string + p_string)
    if miller_rabin_is_prime(num1) and miller_rabin_is_prime(num2):
        return True
    return False


def get_prime_pairs(
    primes: list[int],
) -> tuple[dict[int, list[int]], set[tuple[int, int]]]:
    """
    Get a dictionary of prime keys and lists where each value in the list is
    prime-concatenable with its prime key. Also get a set of 2-tuples which
    are prime-concatenable.
    """
    len_primes = len(primes)
    pairs = defaultdict(list)
    set_pairs = set()
    for i, p in enumerate(primes):
        next_primes = []
        for j in range(i + 1, len_primes):
            q = primes[j]
            if not is_pair(p, q):
                continue
            next_primes.append(q)
            set_pairs.add((p, q))
        if len(next_primes) > 3:
            pairs[p].extend(next_primes)
    return pairs, set_pairs


class PrimeConcatenableFive:
    """Find 5 pairwise prime-concatenable pairs for a given list of primes."""

    def __init__(self, primes: list[int]):
        results = get_prime_pairs(primes)
        self.adj_pairs: dict[int, list[int]] = results[0]
        self.set_pairs: set[tuple[int, int]] = results[1]

    def can_pair(self, prs: tuple[int, ...], x: int) -> bool:
        """Check if x is pairwise prime-concatenable with every pr in prs."""
        return all((pr, x) in self.set_pairs for pr in prs)

    def get_five(self) -> set[tuple[int, int, int, int, int]]:
        """Get a set of 5-tuples which are pairwise prime-concatenable."""
        triples = self._prime_triples()
        quadruples = self._prime_quads(triples)
        return self._prime_quins(quadruples)

    def generate_prime_pairs(self) -> Generator[tuple[int, int], None, None]:
        """Generate prime-concatenable pairs p and q."""
        for p, p_pairs in self.adj_pairs.items():
            for q in p_pairs:
                if (p, q) in self.set_pairs:
                    yield p, q

    def generate_prime_triples(
        self, triples: dict[int, dict[int, list[int]]]
    ) -> Generator[tuple[int, int, int], None, None]:
        """Generate prime-concatenable pairs p, q and r."""
        for p, p_pairs in triples.items():
            for q, q_pairs in p_pairs.items():
                for r in q_pairs:
                    if self.can_pair((p, q), r):
                        yield p, q, r

    def generate_prime_quads(
        self, quads: dict[int, dict[int, dict[int, list]]]
    ) -> Generator[tuple[int, int, int, int], None, None]:
        """Generate prime-concatenable pairs p, q and r."""
        for p, triple in quads.items():
            for q, pair in triple.items():
                for r, r_pairs in pair.items():
                    for s in r_pairs:
                        if self.can_pair((p, q, r), s):
                            yield p, q, r, s

    def _prime_triples(self) -> dict[int, dict[int, list[int]]]:
        """Return a 3-deep, pairwise prime-concatenable integer dict."""
        triples = defaultdict(dict)
        for p, q in self.generate_prime_pairs():
            next_primes = []
            for r in self.adj_pairs.get(q, []):
                if (p, r) not in self.set_pairs:
                    continue
                next_primes.append(r)
            if len(next_primes) > 2:
                triples[p][q] = next_primes
        return triples

    def _prime_quads(
        self, triples: dict[int, dict[int, list[int]]]
    ) -> dict[int, dict[int, dict[int, list]]]:
        """Return a 4-deep, pairwise prime-concatenable integer dict."""
        quads = defaultdict(dict)
        for p, q, r in self.generate_prime_triples(triples):
            next_primes = []
            for s in self.adj_pairs.get(r, []):
                if not self.can_pair((p, q), s):
                    continue
                next_primes.append(s)
            if len(next_primes) > 1:
                if q not in quads.get(p, {}):
                    quads[p][q] = {}
                quads[p][q][r] = next_primes
        return quads

    def _prime_quins(
        self, quads: dict[int, dict[int, dict[int, list]]]
    ) -> set[tuple[int, int, int, int, int]]:
        """Get a set of 5-tuples which are pairwise prime-concatenable."""
        quins = set()
        for p, q, r, s in self.generate_prime_quads(quads):
            for t in self.adj_pairs.get(s, []):
                if self.can_pair((p, q, r), t):
                    quins.add((p, q, r, s, t))
        return quins


def sum_min_five_prime_pairs() -> int:
    """Get the lowest sum of 5 primes which pairwise concatenate to a prime."""
    primes = get_primes(10**4)
    # prime mod 3 = 1 must concatenate to prime mod 3 = 1
    # prime mod 3 = 2 must concatenate to prime mod 3 = 2
    one_primes = [3] + [p for p in primes if p % 3 == 1]
    two_primes = [3] + [p for p in primes if p % 3 == 2]

    prime_concatenable = PrimeConcatenableFive(one_primes)
    solutions = prime_concatenable.get_five()

    prime_concatenable = PrimeConcatenableFive(two_primes)
    solutions |= prime_concatenable.get_five()
    return min(sum(plist) for plist in solutions)
