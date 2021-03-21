# question link: https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.station_total = defaultdict(int)
        self.count = defaultdict(int)
        self.id = {}
        self.id_t = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id[id] = stationName
        self.id_t[id] = t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        key = self.id.pop(id) + stationName
        start_t = self.id_t.pop(id)
        self.station_total[key] += t - start_t
        self.count[key] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + endStation
        return self.station_total[key] / self.count[key]
