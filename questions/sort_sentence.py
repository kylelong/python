def sortSentence(s: str) -> str:
    words = s.split(' ')
    result = [''] * len(words)
    for w in words:
        index = int(w[-1])
        word = w[:len(w) - 1]
        result[index - 1] = word
    return ' '.join(result)

sentence = "is2 This1 sentence4 a3"
print(sortSentence(sentence))