# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s = [i for i in s]
        def giveCount(substring, points):
            nonlocal s
            stack = []
            v = 0
            for i in range(len(s)):
                if s[i] == substring[1] and stack and s[stack[-1]] == substring[0]:
                    a = i
                    b = stack.pop()
                    s[a] = ''
                    s[b] = ''
                    v += points
                else:
                    if s[i] != '':
                        stack.append(i)
            return v
        
        if x > y:
            return giveCount(['a', 'b'], x) + giveCount(['b', 'a'], y)
        else:
            return giveCount(['b', 'a'], y) + giveCount(['a', 'b'], x)