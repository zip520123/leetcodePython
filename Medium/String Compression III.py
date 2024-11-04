# String Compression III
# O(n), O(n)
def compressedString(self, word: str) -> str:
    stack = []
    res = ""
    for char in word:
        if stack:
            curr, count = stack.pop(-1)
            if curr == char and count + 1 <= 9:
                stack.append((curr, count + 1))
            elif curr != char:
                res += str(count)
                res += curr
                stack.append((char, 1))
            elif count + 1 > 9:
                res += str(count)
                
                res += curr
                stack.append((char, 1))
        else:
            stack.append((char, 1))
    curr, count = stack.pop(0)
    res += str(count)
    res += curr
    return res

# O(n), O(1)
def compressedString(self, word: str) -> str:
    res = ""
    curr = word[0]
    count = 1
    for i in range(1, len(word)):
        char = word[i]
        if char == curr and count + 1 <= 9:
            count += 1
        else:
            res += str(count)
            res += curr
            curr = char
            count = 1
    
    res += str(count)
    res += curr
    return res