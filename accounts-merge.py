# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        nameEmail = {}
        parent = {}
        size = defaultdict(int)
        collection = defaultdict(list)


        for c in accounts:
            for n in range(1, len(c)):
                nameEmail[c[n]] = c[0]
                parent[c[n]] = c[n]

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return 
            elif size[pa] >= size[pb]:
                parent[pb] = pa
                size[pa] += size[pb]
            else:
                parent[pa] = pb
                size[pb] += size[pa]


        for i in accounts:
            for j in range(2, len(i)):
                union(i[j-1], i[j])


        
        for i in parent:
            p = find(i)
            collection[p].append(i)
        res = []
        for key in collection:
            res.append([nameEmail[collection[key][0]]] + sorted(collection[key]))
        return res
        
