import string
from string import punctuation
from collections import defaultdict
def words_count(text: str) -> dict:

    s = defaultdict(int)
    text = text.lower()
    for i in punctuation:
        if i in punctuation:
            text = text.replace(i,"")
    words = text.split()
    for word in words:
       s[word] += 1
    return s

result = words_count("This is simple very simple, text very Simple")
print(result)
