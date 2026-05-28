class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for num in operations:
            if num == "+":
                stack.append(int(stack[-1])+int(stack[-2]))
            elif num == "D":
                stack.append(2*int(stack[-1]))
            elif num=="C":
                stack.pop()
            else:
                stack.append(int(num))
            print("s=", stack)
        print(stack)
        return sum(stack)