class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # No matching opening bracket, set new base
                    stack.append(i)
                else:
                    # Calculate the length of the valid substring
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len