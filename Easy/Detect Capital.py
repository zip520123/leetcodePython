# Detect Capital
# O(n), O(1)
def detectCapitalUse(self, word: str) -> bool:
    
    def isCaptial(ch: chr) -> bool:
        return ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    allCapitals = True
    for char in word:
        if isCaptial(char) == False:
            allCapitals = False
    
    allNotCap = True
    for char in word:
        if isCaptial(char) == True:
            allNotCap = False
    
    case3 = True
    if isCaptial(word[0]) == False:
        case3 = False
    for i in range(1, len(word)):
        if isCaptial(word[i]):
            case3 = False
    
    return allCapitals or allNotCap or case3