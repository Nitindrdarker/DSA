# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        tcounter = {}
        scounter = {}
        for i in t:
            tcounter[i] = tcounter.get(i, 0) + 1
        need = len(tcounter)
        have = 0
        left = 0
        res = [-1, -1]
        # def match():#O(26)
        #     for i in tcounter:
        #         if i not in scounter or scounter[i] < tcounter[i]:
        #             return False
        #     return True
        for right in range(len(s)):
            scounter[s[right]] = scounter.get(s[right], 0) + 1
            if s[right] in tcounter and tcounter[s[right]] == scounter[s[right]]:
                have += 1
            while(left <= right and need == have):
                # print(s[left: right + 1], tcounter, scounter)
                if res == [-1 ,-1] or res[1] - res[0] + 1 > (right - left + 1):
                    res = [left, right]
                if s[left] in tcounter and tcounter[s[left]] == scounter[s[left]]:
                    have -= 1
                scounter[s[left]] -= 1
                
                if scounter[s[left]] == 0:
                    del scounter[s[left]]
                left += 1
        return s[res[0]:res[1] + 1] if res != [-1, -1] else ""
                
