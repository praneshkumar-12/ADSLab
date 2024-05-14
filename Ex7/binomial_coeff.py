# Dynamic Programming - Bottom Up
def binomialCoeffDP(n, k):
    # Initialize a 2D array to store calculated binomial coefficients
    C = [[0 for x in range(k+1)] for x in range(n+1)]

    # Iterate over each row (n) and column (k) of the array
    for i in range(n+1):
        for j in range(min(i,k)+1):
            # Base cases: if k is 0 or k is equal to n, set coefficient to 1
            if j == 0 or i == j:
                C[i][j] = 1
            else:
                # Calculate coefficient using the formula C(n, k) = C(n-1, k-1) + C(n-1, k)
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    
    # Return the computed binomial coefficient C(n, k)
    return C[n][k]

# Memoization - Top Down
def binomialCoeffMemoization(n, k, dp):
    # If the value is already computed, return it
    if dp[n][k] != -1:
        return dp[n][k]

    # Base cases: if k is 0 or k is equal to n, set coefficient to 1
    if k == 0:
        dp[n][k] = 1
        return dp[n][k]

    if k == n:
        dp[n][k] = 1
        return dp[n][k]

    # Calculate coefficient using recursive calls with memoization
    dp[n][k] = binomialCoeffMemoization(n - 1, k - 1, dp) + binomialCoeffMemoization(n - 1, k, dp)
    
    # Return the computed binomial coefficient C(n, k)
    return dp[n][k]

def main():
    n = 5
    k = 2

    # Dynamic Programming approach
    result_dp = binomialCoeffDP(n, k)
    print("Binomial coefficient using dynamic programming:", result_dp)

    # Memoization approach
    dp = [[-1 for _ in range(k+1)] for _ in range(n+1)]
    result_memoization = binomialCoeffMemoization(n, k, dp)
    print("Binomial coefficient using memoization:", result_memoization)

if __name__ == "__main__":
    main()