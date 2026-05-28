class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dict = defaultdict(list)
        wordList.append(beginWord)
        q = deque([beginWord])

        # storin pattern in dict
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                dict[pattern].append(word) # all words having same pattern are stored correspondingly

        print(dict)
        res = 1
        print(q)
        visit = set()
        visit.add(beginWord)
        while q:
          for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for nei in dict[pattern]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
          res+=1
        return 0


        
