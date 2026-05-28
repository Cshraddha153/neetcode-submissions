class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p,s) for p, s in zip(position, speed)]
        print("pair", pair)
        # pair.sort(key = p for p, s in range(pair))
        pair = sorted(pair)
        print("pair", pair)
        for p, s in reversed(pair):
            stack.append((target-p)/s)
            while len(stack)>=2 and stack[-1]<=stack[-2]: 
                stack.pop()
            print("stack", stack)
        return len(stack)

