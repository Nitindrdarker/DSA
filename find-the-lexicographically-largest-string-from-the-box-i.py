class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        if numFriends > len(word):
            return ""

        target = len(word) - (numFriends - 1)
        ans = ""
        for i in range(len(word)):
            temp = word[i:i + target]
            # print(temp, target)
            if temp > ans:
                ans = temp
        return ans