class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy solution
        goal = len(nums)-1
        print("goal 1 ",goal)
        for i in range(len(nums)-1, -1, -1):
            print(i)
            if i + nums[i] >= goal:
                goal = i
                print("goal22 ",goal)
        return True if goal == 0 else False