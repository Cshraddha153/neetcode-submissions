class Solution:
    def decodeString(self, s: str) -> str:
        # RECURSION
        self.i = 0
        def helper():
            res = ""
            k=0
            while self.i < len(s):
                c= s[self.i]
                if c.isdigit():
                    k=k*10 + int(c)
                elif c == "[":
                    self.i+=1
                    res+=k*helper()
                    k=0
                elif c=="]":
                    return res
                else:
                    res+=c
                
                self.i += 1
            return res
        return helper()


        # ONE STACK
        # stack = []
        # for i in range(len(s)):
        #     if s[i] != "]":
        #         stack.append(s[i])
        #     else:
        #         substr = ""
        #         while stack[-1] != "[":
        #             substr = stack.pop() + substr
        #         stack.pop()

        #         k=""
        #         while stack and stack[-1].isdigit():
        #             k = stack.pop() + k
        #         stack.append(int(k)*substr)
        # return "".join(stack)




        # str_stack = []
        # count_stack = []
        # cur = ""
        # k=0
        # for c in s:
        #     if c.isdigit():
        #         k = k*10 + int(c)
        #     elif c == "[":
        #         str_stack.append(cur)
        #         count_stack.append(k)
        #         cur = ""
        #         k = 0
        #     elif c == "]":
        #         temp = cur
        #         cur = str_stack.pop()
        #         count = count_stack.pop()
        #         cur += temp*count
                
        #     else:
        #         cur += c
        # return cur