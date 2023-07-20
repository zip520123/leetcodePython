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