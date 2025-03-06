import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.postedTweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.postedTweets[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        maxHeap = []
        totalTweets = 10
        followersList = set()

        if userId in self.followers:
            followersList = self.followers[userId]
        followersList.add(userId) 

        for follower in followersList:
            followerPostedTweets = self.postedTweets[follower]

            for followerPostedTweet in followerPostedTweets:
                heapq.heappush(maxHeap, followerPostedTweet)
        

        while maxHeap or len(tweets) < 10:
            if not maxHeap or len(tweets) == 10:
                break

            prt, tweetId = heapq.heappop(maxHeap)
            tweets.append(tweetId)

        return tweets


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)