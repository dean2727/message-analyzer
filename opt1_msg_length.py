# Average message length analysis
def msgLengthAnalysis(df):
    lengthSum = 0
    for num in df['length'].tolist():
        # Some error length fields could exist, so make sure its an alpha
        if num.isnumeric():
            lengthSum += int(num)
    avgMsgLength = lengthSum / len(df['Message'].tolist())
    print("Average message length (in characters):", round(avgMsgLength))
    print()