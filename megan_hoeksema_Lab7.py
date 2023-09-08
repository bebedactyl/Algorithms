from time import time

# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0:  # The base case
        return 0
    else:  # The recursive case
        minCoins = float("inf")
        for currentCoin in coins:  # Check all coins
            # If we can give change
            if (amount - currentCoin) >= 0:
                # Calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount - currentCoin) + 1
                # Keep the best
                minCoins = min(minCoins, currentMin)
        return minCoins


# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
    # Create the initial tables
    minNumberCoins = [0 for i in range(amount + 1)]
    traceback = [0 for i in range(amount + 1)]

    # Fill in the base case(s)
    minNumberCoins[0] = 0
    traceback[0] = 0

    # Fill in the rest of the table
    for i in range(1, amount + 1):
        minNumberCoins[i] = float('inf')
        traceback[i] = float('inf')

    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                result = minNumberCoins[i - coins[j]]
                if result != float('-inf') and result + 1 < minNumberCoins[i]:
                    minNumberCoins[i] = result + 1
                    traceback[i] = coins[j]

    # print(minNumberCoins)
    # print(traceback[-1])

    i = amount
    while i != 0:
        print(traceback[i])
        i = i - traceback[i]

    if minNumberCoins[amount] == float('-inf'):
        return -1

    return minNumberCoins[amount]

C = [1, 5, 10, 12, 25]  # coin denominations (must include a penny)
A = int(input('Enter desired amount of change: '))
assert A >= 0
print("DAC:")
t1 = time()
numCoins = DACcoins(C, A)
t2 = time()
print("optimal:", numCoins, " in time: ", round((t2 - t1) * 1000, 1), "ms")

print()
print("DP:")
t1 = time()
numCoins = DPcoins(C,A)
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")