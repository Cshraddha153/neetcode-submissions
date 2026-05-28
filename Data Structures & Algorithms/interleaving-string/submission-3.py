class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(i, j, k):
            if k == len(s3):
                return (i==len(s1)) and (j==len(s2))
            
            if i<len(s1) and s1[i]==s3[k]:
                if dfs(i+1, j, k+1):
                    return True
            if j<len(s2) and s2[j]==s3[k]:
                if dfs(i, j+1, k+1):
                    return True
                    
            return False

        return dfs(0, 0, 0)











        # if len(s1)+len(s2)!=len(s3):
        #     return False
        # l=0
        # r=0       GARBAGE CODE
        # while l<(len(s1)) or r<len(s2) or l+r < len(s3):
        #     if l<len(s1) and s1[l]==s3[l+r]:
        #         l+=1
        #     elif r<len(s2) and s2[r]==s3[l+r]:
        #         r+=1
        #     else:
        #         return False
        # return True

