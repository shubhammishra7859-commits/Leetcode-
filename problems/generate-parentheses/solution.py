class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(current_string, open_n, close_n):
            # Base case: if the string has reached the maximum length (2 * n)
            if len(current_string) == 2 * n:
                res.append(current_string)
                return
            
            # Add an opening parenthesis if we haven't used all n of them
            if open_n < n:
                backtrack(current_string + "(", open_n + 1, close_n)
                
            # Add a closing parenthesis if there are unmatched opening parentheses
            if close_n < open_n:
                backtrack(current_string + ")", open_n, close_n + 1)
                
        backtrack("", 0, 0)
        return res