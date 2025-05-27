# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.


from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxVal = 0
        for i in trips:
            maxVal = max(maxVal, i[2])

        res = [0 for i in range(maxVal + 2)]

        for c,f,t in trips:
            res[f] += c
            res[t] -= c

        # total sum
        for i in range(len(res)):
            if i > 0:
                res[i] = res[i-1] + res[i]
            if res[i] > capacity:
                return False
        return True
        
