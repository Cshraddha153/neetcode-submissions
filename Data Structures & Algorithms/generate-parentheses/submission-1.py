class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(i, open, close, curr):
            if i == 2 * n:
                res.append("".join(curr[:]))
                return
            
            if open<n:
                curr.append("(")
                backtrack(i+1, open+1, close, curr)
                curr.pop()
            
            if close<open:
                curr.append(")")
                backtrack(i+1, open, close+1, curr)
                curr.pop()
        
        backtrack(0, 0, 0, [])
        return res
