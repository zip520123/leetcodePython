# String Matching in an Array
# O(n^2) time O(n) space, KMP
def stringMatching(self, words: List[str]) -> List[str]:
    
    seen = set()
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            w1, w2 = words[i], words[j]
            if len(w1) > len(w2):
                w1, w2 = w2, w1
            table = self.longest_selfsequence_table(w1)
            l, r = 0, 0
            while r < len(w2):
                if w1[l] == w2[r]:
                    l += 1
                    r += 1
                    if l == len(w1):
                        seen.add(w1)
                        break
                        l = table[l - 1]
                else:
                    if l > 0:
                        l = table[l - 1]
                    else:
                        r += 1
            
    return list(seen)

def longest_selfsequence_table(self, s) -> List[int]:
    res = [0] * len(s)
    i, length = 1, 0
    while i < len(s):
        if s[i] == s[length]:
            length += 1
            res[i] = length
            i += 1
        else:
            if length > 0:
                length = res[length - 1]
            else:
                i += 1
    return res 


# 
def stringMatching(self, words):
    matching_words = []

    for current_word_index in range(len(words)):
        for other_word_index in range(len(words)):
            if current_word_index == other_word_index:
                continue
            main_word, sub_word = words[current_word_index], words[other_word_index] 
            
            if self.isSubstring(main_word, sub_word):
                matching_words.append(main_word)
                break

    return matching_words

def isSubstring(self, main, sub) -> bool:
    for i in range(len(sub)):
        subfit = True
        for j in range(len(main)):
            if i+j >= len(sub) or sub[i+j] != main[j]:
                subfit = False
                break
        if subfit:
            return True
    return False

# 
def stringMatching(self, words):
    matching_words = []

    for current_word_index in range(len(words)):
        for other_word_index in range(len(words)):
            if current_word_index == other_word_index:
                continue
            main_word, sub_word = words[current_word_index], words[other_word_index] 
            
            if main_word in sub_word:
                matching_words.append(main_word)
                break

    return matching_words