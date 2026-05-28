class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        def backtrack(openbracket, closedbracket):
            if openbracket ==  closedbracket == n:
                temp.append("".join(res))
                return

            if openbracket<n:
                res.append("(")
                backtrack(openbracket + 1, closedbracket)
                res.pop()

            if closedbracket<openbracket:
                res.append(")")
                backtrack(openbracket, closedbracket + 1)
                res.pop()
            

        backtrack(0, 0)
        return temp
