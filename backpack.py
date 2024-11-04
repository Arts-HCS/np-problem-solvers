def mochila(weights, values, capacity):
    n = len(weights)
    dp = [[0 for i in range(capacity + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  # Valor máximo que se puede obtener


weights = [1, 2, 3]
values = [60, 100, 120]
capacity = 5
print(mochila(weights, values, capacity))  
