# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.



import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        for i in freq:
            heapq.heappush(heap, (-1 * freq[i], i))
        


        res = []
        while(heap):
            count, ele = heapq.heappop(heap)
            if res and res[-1] == ele:
                if not heap:
                    return ""
                count2, ele2 = heapq.heappop(heap)
                count2 += 1
                res.append(ele2)
                if count2 < 0:
                    heapq.heappush(heap, (count2, ele2))
                heapq.heappush(heap, (count, ele))
            else:
                count += 1
                res.append(ele)
                if count < 0:
                    heapq.heappush(heap, (count, ele))

        return ''.join(res)

                

