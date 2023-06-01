# Design Underground System
class UndergroundSystem:

    def __init__(self):
        self.checkInRecords = {}
        self.average = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInRecords[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInName, checkInTime = self.checkInRecords[id]

        if checkInName+"-"+stationName not in self.average:
            self.average[checkInName+"-"+stationName] = []
        self.average[checkInName+"-"+stationName].append(t-checkInTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        arr = self.average[startStation+"-"+endStation]
        return sum(arr)/len(arr)