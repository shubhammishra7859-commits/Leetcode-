class Solution:

  def countAndSay(self, n: int) -> str:
    current = "1"

    for _ in range(n - 1):
      next_str = []
      i = 0
      length = len(current)

      while i < length:
        count = 1
        # Count consecutive identical characters
        while i + 1 < length and current[i] == current[i + 1]:
          count += 1
          i += 1
        # Append count and character to the next sequence
        next_str.append(str(count) + current[i])
        i += 1

      current = "".join(next_str)

    return current