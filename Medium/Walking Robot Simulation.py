# Walking Robot Simulation
# O(n), O(n)
def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    res = 0
    obsticales_set = set()
    for x, y in obstacles:
        obsticales_set.add((x, y))
    direction = 0
    curr_x, curr_y = 0, 0
    for command in commands:
        if command == -1:
            direction = (direction + 1) % 4
        elif command == -2:
            direction = ((direction - 1) + 4) % 4
        else:
            if direction == 0:
                for _ in range(command):
                    if (curr_x, curr_y + 1) not in obsticales_set:
                        curr_y += 1
            elif direction == 1:
                for _ in range(command):
                    if (curr_x + 1, curr_y) not in obsticales_set:
                        curr_x += 1
            elif direction == 2:
                for _ in range(command):
                    if (curr_x, curr_y - 1) not in obsticales_set:
                        curr_y -= 1
            else:
                for _ in range(command):
                    if (curr_x - 1, curr_y) not in obsticales_set:
                        curr_x -= 1
        res = max(res, curr_x * curr_x + curr_y * curr_y)
    return res