# Asteroid Collision
# O(n),O(1)
def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []

    for n in asteroids:
        if n > 0:
            stack.append(n)
        else:
            while stack and stack[-1] > 0 and stack[-1] < -n:
                stack.pop(-1)
            
            if len(stack) == 0:
                stack.append(n)
            elif stack[-1] < 0:
                stack.append(n)
            elif stack[-1] == -n:
                stack.pop(-1)

    return stack

# O(n),O(n)
def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    res = []
    stack = []
    for i in range(len(asteroids)):
        if asteroids[i] > 0:
            stack.append(i)
        else:
            while stack and abs(asteroids[i]) > asteroids[stack[-1]]:
                stack.pop()
            if stack and asteroids[stack[-1]] == abs(asteroids[i]):
                stack.pop()
            elif len(stack) == 0:
                res.append(asteroids[i])
    for i in stack:
        res.append(asteroids[i])
    return res