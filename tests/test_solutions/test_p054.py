from solutions.p054 import count_player1_wins, load_hands


def test_count_player1_wins():
    hands = load_hands()
    assert count_player1_wins(hands) == 376
