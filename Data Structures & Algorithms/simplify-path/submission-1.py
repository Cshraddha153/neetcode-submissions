class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/":
            print(c)
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur!="" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c
        return "/" + "/".join(stack)





        # stack = []
        # paths = path.split("/")
        # print(paths)

        # for cur in paths:
        #     if cur == "..":
        #         if stack:
        #             stack.pop()
        #     elif cur!="" and cur!=".":
        #         stack.append(cur)
        # return "/" + "/".join(stack)