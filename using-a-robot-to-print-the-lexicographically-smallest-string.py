# You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

# Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
# Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
# Return the lexicographically smallest string that can be written on the paper.

from typing import Counter


class Solution:
    def robotWithString(self, s: str) -> str:
        freq = Counter(s)
        def minToRight(freq):
            for i in range(26):
                ch = chr(i + ord('a'))
                if freq[ch] > 0:
                    return ch
            return 'a'
        stack = []
        res = []
        for ele in s:
            stack.append(ele)
            freq[ele] -= 1
            while(stack and stack[-1] <= minToRight(freq)):
                res.append(stack.pop())
        while stack:
            res.append(stack.pop())

        return ''.join(res)
