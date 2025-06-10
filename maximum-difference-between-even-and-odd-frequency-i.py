# You are given a string s consisting of lowercase English letters.

# Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

# a1 has an odd frequency in the string.
# a2 has an even frequency in the string.
# Return this maximum difference.


from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        maxOdd = maxEven = 0
        minEven = minOdd = len(s)+1
        freq = Counter(s)
        for i in freq:
            if freq[i] % 2:
                maxOdd = max(maxOdd, freq[i])
            else:
                minEven = min(minEven, freq[i])
        return (maxOdd - minEven)
