class Twitter:

    def __init__(self):
        self.t = 0
        self.followM = defaultdict(set) # user_id ->  set of followee_id (user_id)
        self.tweet = defaultdict(list) # user_id -> list of (time, tweet_id)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t += 1
        self.tweet[userId].append((self.t, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # get tweet lists for user_id and followee_ids of this user_id
        # pointers to last element of each of the tweet list
        # add those element to the max_heap if the pointer is valid
        # add most recent tweet to the result
        # repeat this until there are 10 tweets or all the pointers point to -1
        result = []
        max_heap = []

        self.followM[userId].add(userId)

        for user_id in self.followM[userId]:
            if user_id in self.tweet:
                tweet_list = self.tweet[user_id]
                ptr = len(tweet_list) - 1
                t, tweet_id = tweet_list[ptr]
                heapq.heappush(max_heap, (-t, tweet_id, user_id, ptr - 1))
       
        while len(result) < 10 and max_heap:
            recent_tweet = heapq.heappop(max_heap)
            t, tweet_id, user_id, ptr = recent_tweet

            result.append(tweet_id)

            if ptr >= 0:
                tweet_list = self.tweet[user_id]
                t, tweet_id = tweet_list[ptr]
                heapq.heappush(max_heap, (-t, tweet_id, user_id, ptr - 1))
        
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followM[followerId].add(followeeId) 
        # O(1) due to set

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followM[followerId]:
            self.followM[followerId].remove(followeeId)
            # O(1) as well
