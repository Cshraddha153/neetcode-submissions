class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        j=-1
        for a in asteroids:
            while j>=0 and asteroids[j]>0 and a<0:
                if asteroids[j]>abs(a):
                    a=0
                    break
                elif asteroids[j]==abs(a):
                    j-=1
                    a=0
                    break
                else:
                    j-=1
            if a:
                j+=1
                asteroids[j]=a
        return asteroids[:j+1]



        # stack = []
        # for a in asteroids:
        #     while stack and a<0 and stack[-1]>0:
        #         diff = a + stack[-1]
        #         if diff<0:
        #             stack.pop()
        #         elif diff>0:
        #             a=0
        #         else:
        #             a=0
        #             stack.pop()
        #     if a:
        #         stack.append(a)
        # return stack 