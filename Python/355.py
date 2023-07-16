# Initial thoughts
    # Assuming that if you follow somebody, you see their tweets from before when you followed
    # Need way to organize user follows, probably a hash with a set
    # Need way to organize tweets
        # Do hash mapping each user to a set of their tweets
        # Add a timestamp to each tweet

class Twitter:

    def __init__(self):
        self.follows = {}
        self.tweets = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets.keys():
            self.tweets[userId].append((self.timestamp, tweetId))
        else:
            self.tweets[userId] = [(self.timestamp, tweetId)]
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        follow_list = set([userId])
        if userId in self.follows.keys():
            follow_list.update(self.follows[userId])
        
        heap = []
        for i in follow_list:
            if i in self.tweets.keys():
                for j, k in self.tweets[i]:
                    heappush(heap, (-j, k))

        tweet_count = 0
        result = []
        while heap and tweet_count < 10:
            result.append(heappop(heap)[1])
            tweet_count += 1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows.keys():
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows.keys() and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)