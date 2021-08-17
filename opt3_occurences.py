# How many occurences of a certain word?
def wordOccurences(countVectorizer):
    while True:
        targetWord = input("Enter word, or hit \'enter\' to quit >>> ")
        if targetWord == '':
            return
        targetWord = targetWord.lower()
        if targetWord not in countVectorizer.vocabulary_:
            print("Unable to get information for this word! Sorry about that.")
        else:
            print("\'" + targetWord + "\' appears " + countVectorizer.vocabulary_[targetWord] + " times")