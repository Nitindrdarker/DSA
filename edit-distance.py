# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character




class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # if len(word1) == 0 or len(word2) == 0:
        #     return max(len(word1), len(word2))

        # memo = {}
        # def util(i, j):
        #     if i == len(word1):
        #         return len(word2) - j
        #     if j == len(word2):
        #         return len(word1) - i

        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if word1[i] == word2[j]:
        #         memo[(i, j)] = util(i+1, j+1)
        #     else:
        #         #replace
        #         a = util(i+1, j+1)

        #         #deleted
        #         b = util(i+1, j)

        #         #insert
        #         c = util(i, j+1)
        #         memo[(i, j)] = min(a, b, c) + 1
        #     return memo[(i, j)]
                
        # return util(0,0)



        memo = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]

        for i in range(len(word1)):
            memo[i][len(word2)] = len(word1) - i

        for i in range(len(word2)):
            memo[len(word1)][i] = len(word2) - i


        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    memo[i][j] = memo[i+1][j+1]
                else:
                    a = memo[i+1][j]
                    b = memo[i+1][j+1]
                    c = memo[i][j+1]

                    memo[i][j] = min(a, b, c) + 1
        return memo[0][0]


            

            

