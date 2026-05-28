class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # iteration
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleet=1
        past_time = (target-pair[0][0])/pair[0][1]
        for i in range(1, len(pair)):
            curr_time = (target-pair[i][0])/pair[i][1]
            if curr_time>past_time:
                fleet+=1
                past_time = curr_time
        return fleet








        
        
        
        
        
        
        # O(nlogn)=tc  and   sc=O(n)  stack
        stack = []
        pair = [(p,s) for p, s in zip(position, speed)]
        pair = sorted(pair)
        for p, s in reversed(pair):
            stack.append((target-p)/s)
            while len(stack)>=2 and stack[-1]<=stack[-2]: 
                stack.pop()
            print("stack", stack)
        return len(stack)

