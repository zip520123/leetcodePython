# Circular Sentence
# O(n), O(1)
def isCircularSentence(self, sentence: str) -> bool:
    if sentence[0] != sentence[-1]:
        return False
    for i in range(len(sentence)):
        char = sentence[i]
        if char == " " and sentence[i-1] != sentence[i+1]:
            return False
    return True