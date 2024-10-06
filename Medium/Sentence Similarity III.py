# Sentence Similarity III
# O(n), O(n)
def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
    if len(sentence1) < len(sentence2):
        return self.areSentencesSimilar(sentence2, sentence1)
    arr = sentence1.split(" ")
    arr2 = sentence2.split(" ")
    longest_common_prefix = 0
    for i in range(len(arr2)):
        if arr[i] == arr2[i]:
            longest_common_prefix += 1
        else:
            break

    longest_common_suffix = 0
    for i in range(len(arr2)-1, -1, -1):
        if arr[len(arr)-1-(len(arr2)-1-i)] == arr2[i]:
            longest_common_suffix += 1
        else:
            break
    return longest_common_prefix + longest_common_suffix >= len(arr2)