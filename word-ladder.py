# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        h = defaultdict(list)
        for word in [beginWord] + wordList:
            for i in range(len(word)):
                newWord = word[:i] + '*' + word[i+1:]
                h[newWord].append(word)

        q = deque()
        q.append((beginWord, 1))
        visited = set()
        while(q):
            node, t = q.popleft()
            if node == endWord:
                return t
            if node in visited:
                continue
            visited.add(node)
            for i in range(len(node)):
                newWord = node[:i] + '*' + node[i+1:]
                for word in h[newWord]:
                    if word not in visited:
                        q.append((word, t + 1))



        return 0


