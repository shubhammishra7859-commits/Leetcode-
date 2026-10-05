class Solution:

  def isValid(self, s: str) -> bool:
    # Odd length strings can never be balanced
    if len(s) % 2 != 0:
      return False

    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
      if char in mapping:
        # Closing bracket: check top of stack
        top_element = stack.pop() if stack else "#"
        if mapping[char] != top_element:
          return False
      else:
        # Opening bracket: push onto stack
        stack.append(char)

    # Valid if no unmatched opening brackets remain
    return not stack