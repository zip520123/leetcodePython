# Minimum Amount of Time to Collect Garbage
# O(n), O(1)
def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
    g = 0
    distance = 0
    for i in range(len(garbage)):
        if i > 0: 
            distance += travel[i-1]
        curr = garbage[i]
        for char in curr:
            if char == "G":
                g += 1
                g += distance 
                distance = 0
    distance = 0
    p = 0
    for i in range(len(garbage)):
        if i > 0: 
            distance += travel[i-1]
        curr = garbage[i]
        for char in curr:
            if char == "P":
                p += 1
                p += distance 
                distance = 0
    distance = 0
    m = 0
    for i in range(len(garbage)):
        if i > 0: 
            distance += travel[i-1]
        curr = garbage[i]
        for char in curr:
            if char == "M":
                m += 1
                m += distance 
                distance = 0
    return g+p+m