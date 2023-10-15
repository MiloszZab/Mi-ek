def words_count(text: str) -> dict:
    s = {}
    text.lower()
    words = text.split()

    for word in words:
        if word in words:
            s[word] =+ 1
        else:
            s[word] = 1
    return s

 print(words_count("This is simple very simple text very Simple"))




