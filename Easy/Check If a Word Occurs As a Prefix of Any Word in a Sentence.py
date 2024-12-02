# Check If a Word Occurs As a Prefix of Any Word in a Sentence
# O(n), O(n)
def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    arr = sentence.split(" ")
    res = -1
    for i in range(len(arr)):
        word = arr[i]
        l, r = 0, 0
        while l < len(word) and r < len(searchWord):
            if word[l] != searchWord[r]:
                break
            l += 1
            r += 1
        if r == len(searchWord):
            res = i + 1
            break 

    return res