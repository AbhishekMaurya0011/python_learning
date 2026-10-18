# WAP to find numbers of unique words in a set and input is given by the user.
sentence=input("Enter a Sentence: ")
words=set(sentence.lower().split())
print("The Unique Word is: ",words)
print("Total Number Of Unique Word:",len(words))