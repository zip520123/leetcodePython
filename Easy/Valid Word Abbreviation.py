# Valid Word Abbreviation
# O(word+abbr), O(1)
def validWordAbbreviation(self, word: str, abbr: str) -> bool:
    l, r = 0, 0
    ln, rn = len(word), len(abbr)
    while l < ln and r < rn:
        if word[l] == abbr[r]:
            l += 1
            r += 1
        else:
            if abbr[r].isdigit():
                curr = int(abbr[r])
                if curr == 0: return False
                while r+1 < rn and abbr[r+1].isdigit():
                    curr *= 10
                    curr += int(abbr[r+1])
                    r += 1
                r += 1
                l += curr
            else:
                return False
    return l == ln and r == rn