# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.


from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.followeeMap = defaultdict(set)
        self.postsMap = defaultdict(list)
        self.timeStamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)
        self.postsMap[userId].append((self.timeStamp, tweetId))
        self.timeStamp -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        connectedUsers = self.getConnectedUsers(userId)
        
        postsList = []
        for id in connectedUsers:
            postsList.extend(self.postsMap[id])
        # print(userId, connectedUsers, postsList)
        h = [] #maxHeap
        
        for time, post in postsList:
            if len(h) < 10:
                heapq.heappush(h, (-time, post))
            else:
                if -h[0][0] > time:
                    heapq.heappop(h)
                    heapq.heappush(h, (-time, post))
        # print(h)
        res = []
        while h:
            res.append(heapq.heappop(h)[1])
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeMap[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # print(followerId, followeeId, self.followeeMap)
        if followerId in self.followeeMap and followeeId in self.followeeMap[followerId]:
            self.followeeMap[followerId].remove(followeeId)

    def getConnectedUsers(self, userId) -> List[int]:
        return self.followeeMap[userId]

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)