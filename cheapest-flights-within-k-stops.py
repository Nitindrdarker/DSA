# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 


from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        price = [float("inf") for i in range(n)]


        price[src] = 0
        adj = defaultdict(list)
        for s, d, c in flights:
            adj[s].append((d, c))

        q = deque([(0, src, 0)]) # cost, node, stops
        # print(q.popleft())
        while q:
            # print(q)
            cost, node, stop = q.popleft()

            if stop > k:
                continue
            for neigh, w in adj[node]:
                nextW = w + cost
                if price[neigh] > nextW:
                    price[neigh] = nextW
                    q.append((nextW, neigh, stop + 1))

        return price[dst] if price[dst] != float("inf") else -1