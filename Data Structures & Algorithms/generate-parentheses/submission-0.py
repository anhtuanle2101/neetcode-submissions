class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking
        # base case: we have n open parentheses and n close parentheses 
        # condition: we can only add a close parentheses 
        # so that open > close parentheses
        
        result = []
        cur_string = []

        def backtrack(cur_string, open_count, close_count):
            if open_count == n and close_count == n:
                result.append("".join(cur_string))
            
            if open_count < n:
                cur_string.append("(")
                open_count += 1
                backtrack(cur_string, open_count, close_count)
                cur_string.pop()
                open_count -= 1
            
            if close_count < open_count:
                cur_string.append(")")
                close_count += 1
                backtrack(cur_string, open_count, close_count)
                cur_string.pop()
                close_count -= 1
            
        backtrack(cur_string, 0, 0)
        return result
        