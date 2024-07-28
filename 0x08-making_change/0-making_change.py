#!/usr/bin/python3
"""Making Change Module.

This module contains the make_change function to determine the minimum 
number of coins needed to make a given total.
"""


def make_change(coins, total):
    """
    Determine the minimum number of coins needed to make the given total.
    
    Args:
        coins (list): A list of coin denominations.
        total (int): The amount to be made with the given coins.
    
    Returns:
        int: The minimum number of coins needed to make the total, 
        or -1 if it is not possible.
    """
    if total <= 0:
        return 0
    
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(sorted_coins)
    
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    
    return coins_count
