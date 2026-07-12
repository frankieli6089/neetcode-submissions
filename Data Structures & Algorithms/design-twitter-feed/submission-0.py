from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)   # follower -> followees
        self.tweetMap = defaultdict(list)   # user -> [(time, tweetId)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        # User should always see their own tweets
        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if self.tweetMap[followee]:
                idx = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][idx]
                heapq.heappush(maxHeap, (-time, tweetId, followee, idx))

        while maxHeap and len(res) < 10:
            negTime, tweetId, followee, idx = heapq.heappop(maxHeap)
            res.append(tweetId)

            if idx > 0:
                idx -= 1
                time, tweetId = self.tweetMap[followee][idx]
                heapq.heappush(maxHeap, (-time, tweetId, followee, idx))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followMap[followerId].discard(followeeId)