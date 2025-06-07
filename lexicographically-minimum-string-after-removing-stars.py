# You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

# While there is a '*', do the following operation:

# Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
# Return the lexicographically smallest resulting string after removing all '*' characters.



from collections import defaultdict


class Solution:
    def clearStars(self, s: str) -> str:
        s = [i for i in s]
        freq = defaultdict(list)
        # print(freq)

        # O(26)
        def getSmallestToLeft():
            for i in range(26):
                char = chr(ord('a') + i)
                if char in freq and len(freq[char]) > 0:
                    val = freq[char].pop()
                    if len(freq[char]) == 0:
                        del freq[char]
                    return val
        #O(N)
        for i, val in enumerate(s):
            if s[i] == '*':
                smallestIndex = getSmallestToLeft()
                s[smallestIndex] = ''
                s[i] = ''
            else:
                freq[val].append(i)
        return ''.join(s)
            

