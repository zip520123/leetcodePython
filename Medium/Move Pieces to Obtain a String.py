# Move Pieces to Obtain a String
# O(n), O(n)
def canChange(self, start: str, target: str) -> bool:
    start_queue = []
    target_queue = []
    for i in range(len(start)):
        if start[i] != "_":
            start_queue.append((start[i], i))
        if target[i] != "_":
            target_queue.append((target[i], i))

    if len(start_queue) != len(target_queue):
        return False
    while start_queue:
        start_char, start_index = start_queue.pop(0)
        target_char, target_index = target_queue.pop(0)
        if (
            start_char != target_char 
            or (start_char == "L" and start_index < target_index)
            or (start_char == "R" and start_index > target_index)
        ):
            return False
    return True

# O(n), O(1)
def canChange(self, start: str, target: str) -> bool:
    start_index, target_index = 0, 0
    while start_index < len(start) or target_index < len(target):
        while start_index < len(start) and start[start_index] == "_":
            start_index += 1
        while target_index < len(target) and target[target_index] == "_":
            target_index += 1

        if start_index == len(start) or target_index == len(target):
            return start_index == target_index
        
        start_char = start[start_index]
        target_char = target[target_index]
        if (
            start_char != target_char
            or (start_char == "L" and start_index < target_index)
            or (start_char == "R" and start_index > target_index)
        ):
            return False
        start_index += 1
        target_index += 1

    return True