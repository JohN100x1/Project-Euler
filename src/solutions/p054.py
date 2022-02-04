with open("../../res/p054_poker.txt") as f:
    HANDS = f.read().split("\n")[:-1]

VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}
ROYALS = [10, 11, 12, 13, 14]


def get_player1_win_count():
    player1_wins = 0
    for hand in HANDS:
        player1 = hand[:14]
        player2 = hand[15:]

        rank1, vals1 = get_hand_rank(player1)
        rank2, vals2 = get_hand_rank(player2)

        if rank1 > rank2:
            player1_wins += 1
        elif rank1 == rank2:
            for v1, v2 in zip(reversed(vals1), reversed(vals2)):
                if v1 != v2:
                    if v1 > v2:
                        player1_wins += 1
                    break
    return player1_wins


def get_hand_rank(hand):
    values = get_values(hand)
    flush = is_flush(hand)

    # Check Royal Flush
    if flush and values == ROYALS:
        return 9, values

    # Check Straight Flush
    if flush and values == list(range(values[0], values[0] + 5)):
        return 8, values

    # Kind count
    vcounts = {}
    for v in values:
        if v in vcounts:
            vcounts[v] += 1
        else:
            vcounts[v] = 1
    countlist = sorted(vcounts.values())

    # Check Four of a kind
    if countlist == [1, 4]:
        if vcounts[min(vcounts)] == 4:
            values = values[::-1]
        return 7, values

    # Check Full House
    if countlist == [2, 3]:
        if vcounts[min(vcounts)] == 3:
            values = values[::-1]
        return 6, values

    # Check Flush
    if flush:
        return 5, values

    # Check Straight
    if values == list(range(values[0], values[0] + 5)):
        return 4, values

    # Check Three of a kind
    if countlist == [1, 1, 3]:
        values = []
        end_values = []
        for v in vcounts:
            if vcounts[v] != 3:
                values.append(v)
            else:
                end_values.append(v)
        values.append(end_values * 3)
        return 3, values

    # Check Two pairs
    if countlist == [1, 2, 2]:
        values = []
        end_values = []
        for v in vcounts:
            if vcounts[v] != 2:
                values.append(v)
            else:
                end_values.append(v)
        values.append(sorted(end_values * 2))
        return 2, values

    # Check One pair
    if countlist == [1, 1, 1, 2]:
        values = []
        end_values = []
        for v in vcounts:
            if vcounts[v] != 2:
                values.append(v)
            else:
                end_values.append(v)
        values.append(end_values * 2)
        return 1, values

    # High card
    return 0, values


def get_values(hand):
    values = []
    for i in range(0, 13, 3):
        value = VALUES[hand[i]]
        values.append(value)
    return sorted(values)


def is_flush(hand):
    # Same suit
    suit = hand[1]
    for i in range(4, 14, 3):
        if hand[i] != suit:
            return False
    return True


print(get_player1_win_count())
