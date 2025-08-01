# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        left = 0
        res = 0
        for right in range(len(s)):
            h[s[right]] = h.get(s[right], 0) + 1
            maximum = max(h.values())
            while (left <= right and (right - left + 1) - maximum > k):
                h[s[left]] -= 1
                if h[s[left]] == 0:
                    del h[s[left]]

                maximum = max(h.values())
                left += 1
            res = max(res, right - left + 1)
        return res
 
            
        
            