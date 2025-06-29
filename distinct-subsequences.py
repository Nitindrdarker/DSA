# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # memo = {}
        # def util(i, j):
        #     if j == len(t):
        #         return 1
        #     if i == len(s):
        #         return 0

        #     if (i, j) in memo:
        #         return memo[(i,j)]
        #     a = b = 0
        #     if i < len(s) and s[i] == t[j]:
        #         a = util(i+1, j+1)
        #     b = util(i+1, j)
            
        #     memo[(i, j)] = a + b
        #     return memo[(i, j)]
        # return util(0, 0)

        memo = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        for i in range(len(s)+1):
            memo[i][len(t)] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                a = 0
                if s[i] == t[j]:
                    a = memo[i+1][j+1]
                b = memo[i+1][j]
                memo[i][j] = a + b
        # print(memo)
        return memo[0][0]
                

