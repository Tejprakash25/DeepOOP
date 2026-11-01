#Fibonacci Series:

n = int(input("Enter the number of terms: "))
a,b = 0, 1
step_count = 0

for i in range(n):
    print(a, end=" ")
    step_count += 1

    a,b = b, a + b
    step_count += 1

print("\nTotal steps taken:", step_count)

#Knapsack Problem with greedy approach:

def knapsack(weights, values, capacity):
    items = sorted(
        zip(weights, values),
        key = lambda x : x[0]/x[1], 
        reverse = True
    )

    total_value = 0

    for value, weight in items:
        if capacity == 0:
            break

        take = min(weight, capacity)
        total_value += take * (value / weight)
        capacity -= take

    return total_value

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print("Maximum value in Knapsack =", knapsack(weights, values, capacity))