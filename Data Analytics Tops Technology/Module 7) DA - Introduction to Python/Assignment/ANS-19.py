# Write a Python program to count the occurrences of each word in a given sentence

def count_words_occurrences(Str):

    Str = Str.lower()

    import string
    Str = Str.translate(str.maketrans('','',string.punctuation))

    words = Str.split()

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Get string form user 
Str = input("Enter string : ")
counts = count_words_occurrences(Str)

for word, count in counts.items():
    print(f"{word} : {count}")


