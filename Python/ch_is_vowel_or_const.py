def vowel_or_cons(text):
    for ch in text:
        if ch.lower() in "aeiou":
            print("vowel")
        else:
            print("consonent")
vowel_or_cons("I")