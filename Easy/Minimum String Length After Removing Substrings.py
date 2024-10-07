# Minimum String Length After Removing Substrings
# O(n), O(n)
def minLength(self, s: str) -> int:
    queue = []
    for char in s:
        if queue and queue[-1] == "A" and char == "B":
            queue.pop(-1)
        elif queue and queue[-1] == "C" and char == "D":
            queue.pop(-1)
        else:
            queue.append(char)
    return len(queue)