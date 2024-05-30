def countTheWords(text):
    words = text.split()
    return len(words)

boi = input("Please insert your sentence: ")
word_count = countTheWords(boi)
print( "Here's the word", word_count)
