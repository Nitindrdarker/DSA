# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

# You are also given two integers node1 and node2.

# Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

# Note that edges may contain cycles.



from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        minDistMap1 = {}
        minDistMap2 = {}
        visited = set()

        def util(node, curr, minDistMap):
            if node in visited or node == -1:
                return
            visited.add(node)
            minDistMap[node] = min(minDistMap.get(node, float("inf")), curr)
            util(edges[node], curr + 1, minDistMap)
            visited.remove(node)

        util(node1, 0, minDistMap1)
        util(node2, 0, minDistMap2)

        result = -1
        minDist = float("inf")

        for i in range(len(edges)):
            if i in minDistMap1 and i in minDistMap2:
                maxDist = max(minDistMap1[i], minDistMap2[i])
                if maxDist < minDist or (maxDist == minDist and i < result):
                    minDist = maxDist
                    result = i

        return result
