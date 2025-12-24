import time

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):

    result = {}

    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(amount):
    # array of min count of coins for amounts
    min_coins = [0] + [float("inf")] * amount

    # array of last coins used for amounts
    last_coin = [0] * (amount + 1)

    # calculate count for each amount
    for current_sum in range(1, amount + 1):
        for coin in COINS:
            if coin <= current_sum:
                candidate = min_coins[current_sum - coin] + 1
                if candidate < min_coins[current_sum]:
                    min_coins[current_sum] = candidate
                    last_coin[current_sum] = coin

    # return result as dictionary
    result = {}
    remaining = amount

    while remaining > 0:
        coin = last_coin[remaining]
        result[coin] = result.get(coin, 0) + 1
        remaining -= coin

    return result


if __name__ == "__main__":
    amount = 113

    start = time.time()
    greedy_result = find_coins_greedy(amount)
    end = time.time()
    greedy_time_ms = (end - start) * 1000

    start = time.time()
    dynamic_result = find_min_coins(amount)
    end = time.time()
    dynamic_time_ms = (end - start) * 1000

    print(f"Greedy result: {greedy_result}, time: {greedy_time_ms:.3f} ms")
    print(f"DP result: {dynamic_result}, time: {dynamic_time_ms:.3f} ms")

    assert sum(k * v for k, v in greedy_result.items()) == amount
    assert sum(k * v for k, v in dynamic_result.items()) == amount
