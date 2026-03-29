import heapq

class Twitter:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        self.tracking = defaultdict(list)
        # keep track of the time the tweet is posted
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.heap,[-self.time,userId,tweetId])
        self.time +=1
    def getNewsFeed(self, userId: int) -> List[int]:
        count = 0
        tweet_ids = []
        popped = []
        while count < 10 and self.heap:
            popped.append(heapq.heappop(self.heap))
            if popped[-1][1] in self.tracking[userId] or  popped[-1][1] == userId:
                tweet_ids.append(popped[-1][2])
                count+=1
        for d in popped:
            heapq.heappush(self.heap,d)
        return tweet_ids

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.tracking[followerId]:
            self.tracking[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.tracking[followerId]:
            self.tracking[followerId].remove(followeeId)
        
