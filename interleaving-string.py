# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        memo = {}
        if m + n != len(s3):
            return False

        def util(i, j):
            index = i + j
            
            if i >= n and j >= m:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            a = b = False
            if i < n and s1[i] == s3[index]:
                a = util(i + 1, j)
            if j < m and s2[j] == s3[index]:
                b = util(i, j + 1)

            memo[(i, j)] = a or b
            return memo[(i, j)]

        return util(0, 0)