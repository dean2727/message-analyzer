import matplotlib.pyplot as plt
from sentiment_analysis import testBayesModel

def showSentimentChart(messages, bayesModel, countVectorizer):
    ''' Sentiment ranges:
    Very negative => 0% - 10% positive
    Negative => 10% - 40% positive
    Neutral => 40% - 60% positive
    Positive => 60% - 90% positive
    Very positive => 90% - 100% positive
    '''
    labels = ["Very negative 😡", "Negative 😢", "Neutral 😐", "Positive 😊", "Very positive 😄"]
    numVeryNegative, numNegative, numNeutral, numPositive, numVeryPositive = 0, 0, 0, 0, 0

    print("Analyzing messages...")
    for message in messages:
        try:
            pred = testBayesModel(message, bayesModel, countVectorizer)
            pos = pred[0][1] * 100
            if pos <= 10:
                numVeryNegative += 1
            elif pos > 10 and pos <= 40:
                numNegative += 1
            elif pos > 40 and pos < 60:
                numNeutral += 1
            elif pos >= 60 and pos <= 90:
                numPositive += 1
            else:
                numVeryPositive += 1
        except:
            print("Invalid message to analyze: \'" + message + "\'. Ignoring this")

    sizes = [numVeryNegative, numNegative, numNeutral, numPositive, numVeryPositive]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.show()