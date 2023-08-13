def minOperations(n):
    """
    Calculates the fewest number of operations needed to obtain
    exactly n characters 'H' in the text file.
    
    Args:
        n (int): The target number of characters 'H'.
    
    Returns:
        int: Minimum number of operations, or 0 if impossible.
    """
    if n <= 1:
        return 0
    
    # Initialize a dynamic programming array to store the minimum operations
    dp = [0] * (n + 1)
    
    # Populate the dynamic programming array using bottom-up approach
    for i in range(2, n + 1):
        dp[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                # Update dp[i] with the minimum operations
                dp[i] = min(dp[i], dp[j] + i // j)
    
    # If it's impossible to achieve n, return 0
    return dp[n] if dp[n] != float('inf') else 0

