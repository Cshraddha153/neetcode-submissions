class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapp = {i : [] for i in range(numCourses)}
        for crs, preq in prerequisites:
            mapp[crs].append(preq)
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if mapp[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in mapp[crs]:
                if not dfs(pre): return False

            visitSet.remove(crs)
            mapp[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True






















