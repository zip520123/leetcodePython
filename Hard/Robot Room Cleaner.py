# Robot Room Cleaner
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        seen = set()
        x, y = 0, 0
        seen.add((x,y))
        robot.clean()
        def moveBack():
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        direct = [(0,-1),(1,0),(0,1),(-1,0)]
        def dfs(d):
            nonlocal x, y
            for i in range(4):
                newD = (d + i) % 4
                dx, dy = direct[newD]
                if (x+dx,y+dy) not in seen and robot.move():
                    x += dx
                    y += dy
                    seen.add((x, y))
                    robot.clean()
                    dfs(newD)
                    moveBack()
                    x -= dx
                    y -= dy
                robot.turnRight()

        dfs(0)