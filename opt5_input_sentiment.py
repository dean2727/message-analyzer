from sentiment_analysis import testBayesModel

# Let the user see the sentiment of their own texts
def getTestMsgSentiment(trainedBayesModel, countVectorizer):
    while True:
        testMsg = input("Enter your message, or hit \'enter\' to quit >>> ")
        if testMsg == '':
            break
        else:
            pred = testBayesModel(testMsg, trainedBayesModel, countVectorizer)
            neg = pred[0][0]
            pos = pred[0][1]
            print("\'" + testMsg + "\':")
            print(str(round(neg * 100)) + "% negative, " + str(round(pos * 100)) + "% positive")