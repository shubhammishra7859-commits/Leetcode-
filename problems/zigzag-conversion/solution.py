class Solution:

  def convert(self, s: str, numRows: int) -> str:
    # Edge case: if numRows is 1 or greater than/equal to string length, no zigzag needed
    if numRows == 1 or numRows >= len(s):
      return s

    # Initialize a list of empty strings for each row
    rows = ['' for _ in range(numRows)]
    current_row = 0
    going_down = False

    for char in s:
      rows[current_row] += char
      # Change direction when we hit the top or bottom row
      if current_row == 0 or current_row == numRows - 1:
        going_down = not going_down
      # Move down or up depending on the direction flag
      current_row += 1 if going_down else -1

    # Combine all rows into a single string
    return ''.join(rows)