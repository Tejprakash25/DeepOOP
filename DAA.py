# #Fibonacci Series:

# n = int(input("Enter the number of terms: "))
# a,b = 0, 1
# step_count = 0

# for i in range(n):
#     print(a, end=" ")
#     step_count += 1

#     a,b = b, a + b
#     step_count += 1

# print("\nTotal steps taken:", step_count)

# #Knapsack Problem with greedy approach:

# def knapsack(values, weights, capacity):
#     items = sorted(
#         zip(weights, values),
#         key = lambda x : x[0]/x[1], 
#         reverse = True
#     )

#     total_value = 0

#     for value, weight in items:
#         if capacity == 0:
#             break

#         take = min(weight, capacity)
#         total_value += take * (value / weight)
#         capacity -= take

#     return total_value

# values = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50

# print("Maximum value in Knapsack =", knapsack(values, weights, capacity))

# #Knapsack Problem with dynamic programming approach:
# def knapsack_dp(values, weights, capacity):
#     n = len(values)
#     dp = [[0] * (capacity + 1) for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for w in range(capacity + 1):
#             if weights[i-1] <= w:
#                 dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w]) 
#             else:
#                 dp[i][w] = dp[i-1][w]

#     return dp[n][capacity]

# values = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50

# print("Maximum value in Knapsack (DP) =", knapsack_dp(values, weights, capacity))

#N-Queens Problem - Backtracking:

def solve(n):
    board = [[0] * n for _ in range(n)]
    cols, diag1, diag2 = set(), set(), set()

    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                board[row][col] = 1
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                if backtrack(row + 1):
                    return True

                board[row][col] = 0
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        return False

    board[0][0] = 1
    cols.add(0)
    diag1.add(0)
    diag2.add(0)

    if backtrack(1):
        for row in board:
            print(*row)
    else:
        print("No solution exists")

n = int(input("Enter the size of the board (N): "))
solve(n)