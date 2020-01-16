def getLongestWord(p_sentence):
    mylist = p_sentence.split(' ')
    longestWord = ""
    wordList = []

    # retrieve the longest word
    for i in range(len(mylist)): # len gives the size of list
        word = mylist[i]

        if len(word) >= len(longestWord):
            longestWord = word

    # retrieve all words that are same length as longest word
    for i in range(len(mylist)): # len gives the size of list
        word = mylist[i]

        if len(word) == len(longestWord):
            wordList.append(word)

    return wordList


while True: #indefinite loop
    sentence = input("Enter your sentence or type 'quit' to exit")
    if sentence.lower() != "quit":
        myLongestWord = getLongestWord(sentence)
        print(myLongestWord)
    else:
        break
