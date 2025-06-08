# You are given an array complexity of length n.

# There are n locked computers in a room with labels from 0 to n - 1, each with its own unique password. The password of the computer i has a complexity complexity[i].

# The password for the computer labeled 0 is already decrypted and serves as the root. All other computers must be unlocked using it or another previously unlocked computer, following this information:

# You can decrypt the password for the computer i using the password for computer j, where j is any integer less than i with a lower complexity. (i.e. j < i and complexity[j] < complexity[i])
# To decrypt the password for computer i, you must have already unlocked a computer j such that j < i and complexity[j] < complexity[i].
# Find the number of permutations of [0, 1, 2, ..., (n - 1)] that represent a valid order in which the computers can be unlocked, starting from computer 0 as the only initially unlocked one.

# Since the answer may be large, return it modulo 109 + 7.

# Note that the password for the computer with label 0 is decrypted, and not the computer with the first position in the permutation.

# A permutation is a rearrangement of all the elements of an array.

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.©leetcode




from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10 ** 9 + 7
        def calcFact(k):
            res = 1
            for i in range(1, k+1):
                res = (res * i) % mod
            return res % mod
        limit = complexity[0]
        for i in range(1, len(complexity)):
            if complexity[i] <= limit:
                return 0
        return calcFact(len(complexity) - 1) % mod