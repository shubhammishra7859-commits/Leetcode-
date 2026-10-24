class Solution:

  def isValidSudoku(self, board: list[list[str]]) -> bool:
    seen = set()

    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val == ".":
          continue

        # Define unique keys for row, column, and 3x3 sub-box
        row_key = (r, val)
        col_key = (val, c)
        box_key = (r // 3, c // 3, val)

        # Check if any duplicate exists
        if row_key in seen or col_key in seen or box_key in seen:
          return False

        # Add keys to our tracking set
        seen.add(row_key)
        seen.add(col_key)
        seen.add(box_key)

    return True