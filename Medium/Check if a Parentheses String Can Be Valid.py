# Check if a Parentheses String Can Be Valid
# O(n), O(n)
def canBeValid(self, s: str, locked: str) -> bool:
    if len(s) % 2 == 1:
        return False

    unlock = []
    l = []

    for i in range(len(s)):
        if locked[i] == "0":
            unlock.append(i)
        else:
            if s[i] == "(":
                l.append(i)
            else:
                if l:
                    l.pop()
                elif unlock:
                    unlock.pop()
                else:
                    return False
    
    while l and unlock and l[-1] < unlock[-1]:
        l.pop()
        unlock.pop()
    if l:
        return False
    return True