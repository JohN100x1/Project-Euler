from collections import defaultdict

from config import path_res

VALUES = {str(i): i for i in range(2, 10)}
VALUES.update({"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14})
ROYALS = [10, 11, 12, 13, 14]


def load_hands() -> list[str]:
    """Loads a list of strings from /res/p054_poker.txt."""
    with open(path_res / "p054_poker.txt") as f:
        return f.read().split("\n")[:-1]


def is_flush(hand: str) -> bool:
    """Check if the hand have the same suit."""
    suit = hand[1]
    for i in range(4, 14, 3):
        if hand[i] != suit:
            return False
    return True


def get_values(hand: str) -> list[int]:
    """Get the values of the hand as a list of integers."""
    values = []
    for i in range(0, 13, 3):
        value = VALUES[hand[i]]
        values.append(value)
    return sorted(values)


def get_hand_rank(hand: str) -> tuple[int, list[int]]:
    """Get the rank and values of the hand."""
    values = get_values(hand)
    flush = is_flush(hand)

    # Check Royal Flush
    if flush and values == ROYALS:
        return 9, values

    # Check Straight Flush
    if flush and values == list(range(values[0], values[0] + 5)):
        return 8, values

    # Kind count
    value_count = defaultdict(int)
    for v in values:
        value_count[v] += 1
    count_list = sorted(value_count.values())

    # Check Four of a kind
    if count_list == [1, 4]:
        if value_count[min(value_count)] == 4:
            values = values[::-1]
        return 7, values

    # Check Full House
    if count_list == [2, 3]:
        if value_count[min(value_count)] == 3:
            values = values[::-1]
        return 6, values

    # Check Flush
    if flush:
        return 5, values

    # Check Straight
    if values == list(range(values[0], values[0] + 5)):
        return 4, values

    # Check Three of a kind
    if count_list == [1, 1, 3]:
        values = []
        end_values = []
        for v in value_count:
            if value_count[v] != 3:
                values.append(v)
            else:
                end_values.append(v)
        values.append(end_values * 3)
        return 3, values

    # Check Two pairs
    if count_list == [1, 2, 2]:
        values = []
        end_values = []
        for v in value_count:
            if value_count[v] != 2:
                values.append(v)
            else:
                end_values.append(v)
        values.append(sorted(end_values * 2))
        return 2, values

    # Check One pair
    if count_list == [1, 1, 1, 2]:
        values = []
        end_values = []
        for v in value_count:
            if value_count[v] != 2:
                values.append(v)
            else:
                end_values.append(v)
        values.append(end_values * 2)
        return 1, values

    # High card
    return 0, values


def count_player1_wins(hands: list[str]) -> int:
    """Get the number of poker hand wins for player 1."""
    player1_wins = 0
    for hand in hands:
        player1 = hand[:14]
        player2 = hand[15:]

        rank1, vals1 = get_hand_rank(player1)
        rank2, vals2 = get_hand_rank(player2)

        if rank1 > rank2:
            player1_wins += 1
        elif rank1 == rank2:
            for v1, v2 in zip(reversed(vals1), reversed(vals2)):
                if v1 == v2:
                    continue
                elif v1 > v2:
                    player1_wins += 1
                break
    return player1_wins
