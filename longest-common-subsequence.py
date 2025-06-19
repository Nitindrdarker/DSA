# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for i in range(len(text2))] for j in range(len(text1))]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + (memo[i+1][j+1] if (i+1 < len(text1) and j+1 < len(text2)) else 0)
                else:
                    down = memo[i+1][j] if i + 1 < len(text1) else 0
                    right = memo[i][j+1] if j + 1 < len(text2) else 0
                    memo[i][j] = max(down, right)
        return memo[0][0]






        # memo = {}
        # def util(i, j):
        #     if i >= len(text1) or j >= len(text2):
        #         return 0
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     val = 0

        #     if text1[i] == text2[j]:
        #         val = 1 + util(i+1, j+1)
        #     else:
        #         val = max(util(i+1, j), util(i, j+1))
        #     memo[(i,j)] = val
        #     return val
        # return util(0, 0)