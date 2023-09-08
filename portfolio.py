# When using the Zillow file, please use the 10 year estimate to calculate your profit.
# Only purchase 1 house per state.  And you have 1 million dollars to spend.
# Please include the results of thus run in your submission (separate file or in the comments).

import csv

def loadInvestments():
    """Returns a list of possible investment options: Name, Cost, Estimated Return"""
    filename = open('State_Zhvi_Summary_AllHomes.csv', 'r')
    file = csv.DictReader(filename)

    # Creates the lists of data needed
    listOfInvestments = []
    cost = []
    estimatedReturn = []

    # Adds the corresponding column of data to the lists
    for col in file:
        listOfInvestments.append(col['RegionID'])
        cost.append(col['Zhvi'])
        estimatedReturn.append(col['10Year'])

    # Remove first item of each list, don't need them
    listOfInvestments.pop(0)
    cost.pop(0)
    estimatedReturn.pop(0)

    cost = [int(i) for i in cost]
    estimatedReturn = [float(j) for j in estimatedReturn]

    return listOfInvestments, cost, estimatedReturn

def optimizeInvestments(listOfInvestments, moneyToSpend):
    """Returns the optimal return on investment and the investments selected to achieve optimal return"""
    listOfInvestments, cost, estimatedReturn = loadInvestments()

    n = len(cost)
    portfolio = [[0 for x in range(moneyToSpend + 1)] for x in range(n+1)]
    traceback = [[0 for x in range(moneyToSpend + 1)] for x in range(n+1)]

    for i in range(n + 1):
        for w in range(moneyToSpend + 1):
            if i == 0 or w == 0:
                portfolio[i][w] = 0
                traceback[i][w] = 0
            elif cost[i - 1] <= w:
                portfolio[i][w] = max(estimatedReturn[i - 1] + portfolio[i - 1][w - cost[i - 1]], portfolio[i - 1][w])
            else:
                portfolio[i][w] = portfolio[i - 1][w]

    result = portfolio[n][moneyToSpend]
    print("Optimal Estimated Return: " + str(result))

    # For traceback
    print('Traceback table:')
    for lst in traceback:
        print(lst)

# Test loadGraph Function
# print(loadInvestments())

# Run
listOfInvestments, cost, estimatedReturn = loadInvestments()
optimizeInvestments(listOfInvestments, 1000000)


# Results
# Optimal Return on Investment: 0.21413197336680118
