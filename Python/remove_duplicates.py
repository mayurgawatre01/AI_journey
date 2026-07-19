def remove_duplicate(text):
    result=""
    for ch in text:
        if ch not in result:
            result+=ch
    return result
print(remove_duplicate("banana"))