def palindrome(text):
    reverse=""
    for ch in text:
        reverse=ch+reverse
    
    print(reverse)
    print(text)
    if text==reverse: return True
    else: return False 
print(palindrome("DataAnalyst"))