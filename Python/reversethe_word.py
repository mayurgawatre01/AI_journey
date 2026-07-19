def reverse_word(text):
    words=text.split()
    words.reverse()
    return " ".join(words)

print(reverse_word("i love you python "))