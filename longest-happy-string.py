# A string s is called happy if it satisfies the following conditions:

# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.



from collections import deque
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        for c, i in ((-a, 'a'), (-b, 'b'), (-c, 'c')):
            if c < 0:
                heapq.heappush(h, (c, i))
        res = []
        while(h):
            count, ele = heapq.heappop(h)
            if len(res) < 2 or res[-1] != ele or res[-2] != ele:
                res.append(ele)
                count += 1
                if count < 0:
                    heapq.heappush(h, (count, ele))
            else:
                if h:
                    count1, ele1 = heapq.heappop(h)
                    res.append(ele1)
                    count1 += 1
                    if count1 < 0:
                        heapq.heappush(h, (count1, ele1))
                else:
                    return ''.join(res)
                heapq.heappush(h, (count, ele))
        return ''.join(res)
                