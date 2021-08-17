import speech_recognition as sr
from sentiment_analysis import testBayesModel
from preprocessing import cleanMessage

# Listen to a user's voice (from default mic) and return speech-to-text
def listenAndTranslate():
    speechRecognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speechRecognizer.adjust_for_ambient_noise(source)
        
        print("Listening...")
        audio = speechRecognizer.listen(source)
        print("Thank you!")

        # Convert speech to text
        try:
            print("Translating speech...")
            text = speechRecognizer.recognize_google(audio)
            return text
        except:
            print("Error occured! Sorry about that!")
            return ""

# Given text (translated from user's speech), get the sentiment of the message
def showSpeechSentiment(text, trainedBayesModel, countVectorizer):
    # First, preprocess the text so it matches the preprocessed training data
    cleaned = cleanMessage(text)
    # Now we can get sentiment
    pred = testBayesModel(cleaned, trainedBayesModel, countVectorizer)
    neg = pred[0][0]
    pos = pred[0][1]
    print("\'" + text + "\':")
    print(str(round(neg * 100)) + "% negative, " + str(round(pos * 100)) + "% positive")
    print()
