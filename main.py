from preprocessing import readMessagesCsv, cleanCorpus
from sentiment_analysis import trainBayesModel, testBayesModel
from word2vec import trainWord2VecModel

from opt1_msg_length import msgLengthAnalysis
from opt2_jargin import msgJarginAnalysis
from opt3_occurences import wordOccurences
from opt4_msg_sentiment import showSentimentChart
from opt5_input_sentiment import getTestMsgSentiment
from opt6_context import showSimilarContextWords
from opt7_questions import getNumQuestions
from opt8_speech import listenAndTranslate, showSpeechSentiment

if __name__ == "__main__":
    trainingSetFile = input("Enter file name (with extension) of training dataset >>> ")
    testingSetFile = input("Enter file name (with extension) of testing dataset (hit \'enter\' if none) >>> ")
    # If no testing set, then the training set = the testing set
    hasTestingSet = True if testingSetFile != "" else False

    # Retrieve pandas dataframe
    datasetPathTraining = './datasets/' + trainingSetFile
    trainingDataFrame = readMessagesCsv(datasetPathTraining)

    # Dataframe is assumed to have the same headers as clean_nus_sms.csv
    messagesTraining = trainingDataFrame['Message'].tolist()
    numTrainingMsgs = len(messagesTraining)

    # Preprocessing to get a list of clean messages
    print("Preprocessing messages from training set...")
    cleanedTextTraining = cleanCorpus(messagesTraining)

    if hasTestingSet:
        datasetPathTesting = './datasets/' + testingSetFile
        testingDataFrame = readMessagesCsv(datasetPathTesting)
        messagesTesting = testingDataFrame['Message'].tolist()
        numTestingMsgs = len(messagesTesting)
        print("Preprcessing messages from test set...")
        cleanedTextTest = cleanCorpus(messagesTesting)

    else:
        cleanedTextTesting = cleanedTextTraining
        numTestingMsgs = numTrainingMsgs
        testingDataFrame = trainingDataFrame
        messagesTesting = messagesTraining

    print("Training models (this may take a moment)...")
    # Training Naive Bayes model with the preprocessed text
    trainedBayesModel, countVectorizer = trainBayesModel(cleanedTextTraining)
    # Training word2vec model for analyzing context/meaning
    w2vModel = trainWord2VecModel(cleanedTextTraining)

    menu = """
    1. See average message length in characters (in testing set)
    2. See number of jargin (non-english) words and 5 most common such words (in testing set)
    3. See # of occurences of specified words (in testing set)
    4. See pie chart of message sentiment (in testing set)
    5. See sentiment of specified messages (based on the training set)
    6. See top 10 words used in similar contexts to a word (in testing set)
    7. See how many messages have questions (in testing set)
    8. Speak into microphone and see how positive/negative your words are (based on training set)
    """

    while True:
        print("~~~~~ CHOOSE AN OPTION BELOW (or hit \'enter\' to quit) ~~~~~")
        print(menu)
        option = int(input())

        if option == 1:
            msgLengthAnalysis(testingDataFrame)
        elif option == 2:
            msgJarginAnalysis(cleanedTextTesting)
        elif option == 3:
            wordOccurences(countVectorizer)
        elif option == 4:
            showSentimentChart(messagesTesting, trainedBayesModel, countVectorizer)
        elif option == 5:
            getTestMsgSentiment(trainedBayesModel, countVectorizer)
        elif option == 6:
            showSimilarContextWords(cleanedTextTesting, w2vModel, 10)
        elif option == 7:
            getNumQuestions(cleanedTextTest, numTestingMsgs)
        elif option == 8:
            userSpeech = listenAndTranslate()
            showSpeechSentiment(userSpeech, trainedBayesModel, countVectorizer)
        else:
            print("Invalid choice!\n")
    
    print("Goodbye! Have a great day :)")


