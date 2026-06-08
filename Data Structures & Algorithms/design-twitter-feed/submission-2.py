class Twitter:

    def __init__(self):
        self.followMap = {}
        self.user2tweet = {}
        self.tweet2user = {}
        self.time = 0
        self.tweet2time = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user2tweet:
            self.user2tweet[userId] = []
        
        self.user2tweet[userId].append(tweetId)
        self.tweet2user[tweetId] = userId
        self.tweet2time[tweetId] = self.time
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []
        # O(N)
        sources = set(self.followMap.get(userId, set()))
        sources.add(userId)
        # get last tweet from each follow
        for currUserId in sources:
            if currUserId not in self.user2tweet or not self.user2tweet[currUserId]:
                continue
            idx = len(self.user2tweet[currUserId])-1
            tweetid = self.user2tweet[currUserId][-1]
            time = self.tweet2time[tweetid]
            heapq.heappush(pq, (-time, tweetid, idx))

        cnt = 0
        res = []
        #print(pq)
        while pq and cnt < 10:
            time, currTweetId, idx = heapq.heappop(pq)
            res.append(currTweetId)
            if idx > 0:
                user = self.tweet2user[currTweetId]

                prevTweetId = self.user2tweet[user][idx-1]
                prevTime = self.tweet2time[prevTweetId]
                heapq.heappush(pq, (-prevTime, prevTweetId, idx-1))
            cnt += 1
        
        return res
        


    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
