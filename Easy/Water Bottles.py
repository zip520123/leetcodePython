# Water Bottles
# O(log numBottles), O(1)
def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    res = numBottles
    curr = numBottles
    while curr >= numExchange:
        res += curr // numExchange
        curr = curr // numExchange + curr % numExchange
    
    return res