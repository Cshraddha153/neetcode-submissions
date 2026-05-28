class Twitter:
    # Tc = O(n log n) for each getNewsFeed for rest O(1)
    #sc = O(N*m + N*M + n)

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userid--> list of [count, tweetIds]
        self.followMap = defaultdict(set) # userid--> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index-1])
            
        while minheap and len(res)<10:
            count, tweetId, followeeId, index =  heapq.heappop(minheap)
            res.append(tweetId)
            if index>=0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
