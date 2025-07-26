# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


import heapq


class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        if len(self.maxHeap) - len(self.minHeap) > 1:
            maxValue = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, maxValue)

        if self.minHeap and -1 * self.maxHeap[0] > self.minHeap[0]:
            maxValue = -1 * heapq.heappop(self.maxHeap)
            minValue = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * minValue)
            heapq.heappush(self.minHeap, maxValue)

    def findMedian(self) -> float:
        total = len(self.minHeap) + len(self.maxHeap)
        if total % 2 == 0:
            a = self.minHeap[0]
            b = -1 * self.maxHeap[0]
            return (a + b) / 2
        return -1 * self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()