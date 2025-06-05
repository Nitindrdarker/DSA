# You are given an integer n. There are n rooms numbered from 0 to n - 1.

# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

# Meetings are allocated to rooms in the following manner:

# Each meeting will take place in the unused room with the lowest number.
# If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
# When a room becomes unused, meetings that have an earlier original start time should be given the room.
# Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

# A half-closed interval [a, b) is the interval between a and b including a and not including b.




import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        avalible_room = [i for i in range(n)]
        busy_room = []
        heapq.heapify(avalible_room)

        meetings.sort()
        meeting_count = [0] * n
        for start, end in meetings:
            while busy_room and busy_room[0][0] <= start:
                e, roomNo = heapq.heappop(busy_room)
                heapq.heappush(avalible_room, roomNo)

            duration = end - start
            if avalible_room:
                roomNo = heapq.heappop(avalible_room)
                heapq.heappush(busy_room, (end, roomNo))
                meeting_count[roomNo] += 1
            elif busy_room:
                endTime, roomNo = heapq.heappop(busy_room)
                newEnd = endTime + duration
                heapq.heappush(busy_room, (newEnd, roomNo))
                meeting_count[roomNo] += 1
        maxMeetingIndex = 0
        for i, val in enumerate(meeting_count):
            if val > meeting_count[maxMeetingIndex]:
                maxMeetingIndex = i
        return maxMeetingIndex
                


