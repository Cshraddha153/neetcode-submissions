class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i, j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i==len(word1):
                return len(word2)-j

            if j ==len(word2):
                return len(word1)-i

            if word1[i]==word2[j]:
                return dfs(i+1, j+1)

            res = min(dfs(i+1, j), dfs(i, j+1))
            res = min(res, dfs(i+1, j+1))
            memo[(i,j)]=res+1
            return res+1

        return dfs(0,0)






        # def dfs(i, j):
        #     if i==len(word1):
        #         return len(word2)-j
        #     if j ==len(word2):
        #         return len(word1)-i
        #     if word1[i]==word2[j]:
        #         return dfs(i+1, j+1)
        #     res = min(dfs(i+1, j), dfs(i, j+1))
        #     res = min(res, dfs(i+1, j+1))
        #     return res+1

        # return dfs(0,0)











        # Tc = O(m*n)   sc=O(m*n)   Dynamic Programming (Bottom-Up)

        grid = [[float("inf")]*(len(word2)+1) for i in range(len(word1)+1)]

        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2)-j
        
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1)-i
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        return dp[0][0]
        













