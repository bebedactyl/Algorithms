import pandas as pd
from collections import defaultdict

def loadData():
    """Reads in data into dataframes"""
    #Dataframe for prices
    df = pd.read_csv("prices-split-adjusted.csv")
    df = df.drop(columns=['open', 'low', 'high', 'volume'])
    # print(df)

    #dataframe for company names
    df2 = pd.read_csv("securities.csv")
    df2 = df2.drop(columns=["SEC filings","GICS Sector","GICS Sub Industry","Address of Headquarters","Date first added","CIK"])
    # print(df2)

    #merge the dataframes according to ticker symbol (adds a column to each row with the company name)
    # mergeDF = df.join(df2.set_index('Ticker symbol'), on='symbol')
    # print(mergeDF)

    #Creates a dictionary
    # dict = mergeDF.groupby('symbol').apply(lambda dfg: dfg.drop('symbol', axis=1).to_dict(orient='list')).to_dict()
    # print(dict)


    value_list = ["WLTW"]
    boolean_series = df.symbol.isin(value_list)
    filtered_df = df[boolean_series]
    # print(filtered_df)
    wltw = filtered_df['close'].tolist()
    # print(wltw)
    return wltw

def max_crossing_subarray(ar, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        sum = sum + ar[i]
        if sum > left_sum:
            left_sum = sum

    right_sum = float('-inf')
    sum = 0
    for i in range(mid + 1, high + 1):
        sum = sum + ar[i]
        if sum > right_sum:
            right_sum = sum

    return left_sum + right_sum


def max_sum_subarray(A, low, high):
    if high == low:
        return A[high]

    mid = (high + low) // 2

    maxLeft = max_sum_subarray(A, low, mid)
    maxRight = max_sum_subarray(A, mid + 1, high)
    maxCross = max_crossing_subarray(A, low, mid, high)

    return max(maxLeft, maxRight, maxCross)



# Test loadData Function
# loadData()

# Test DAC
# A = [3, -1, -1, 10, -3, -2, 4, 25]
# print(max_sum_subarray(A, 0, len(A)-1))

# Assignment 2 Run
B = loadData()
print(max_sum_subarray(B, 0, len(B)-1))

