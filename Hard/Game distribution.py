def getMinSize(gameSize, k) -> int:
    gameSize.sort()
    extra = len(gameSize) % k
    single_game = k-extra
    res = 0
    l, r = 0, len(gameSize)-single_game-1
    while l<r:
        res = max(res, gameSize[l]+gameSize[r])
        l += 1
        r -= 1
    for i in range(len(gameSize)-single_game, len(gameSize)):
        res = max(res, gameSize[i])
    return res
    

assert getMinSize([9,4,2,6], 3) == 9

'''
child 5 game 7
7%5 = 2
extra = game % child
5-2 = 3
single_game = child-extra
max(single_game)
7-3 = 4

child 6 game 7
7%6 = 1 extra 
6-1 = 5 single

child 7 game 7
7%7 = 0 extra
7-0 = 7 single

'''