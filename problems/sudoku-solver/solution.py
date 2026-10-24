class Solution:

  def solveSudoku(self, board: list[list[str]]) -> None:
    """Do not return anything, modify board in-place instead."""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Pre-populate tracking sets with existing board numbers
    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val != ".":
          rows[r].add(val)
          cols[c].add(val)
          boxes[(r // 3) * 3 + (c // 3)].add(val)

    def backtrack(r: int, c: int) -> bool:
      if r == 9:
        return True
      if c == 9:
        return backtrack(r + 1, 0)
      if board[r][c] != ".":
        return backtrack(r, c + 1)

      box_idx = (r // 3) * 3 + (c // 3)

      for digit in map(str, range(1, 10)):
        if (
            digit not in rows[r]
            and digit not in cols[c]
            and digit not in boxes[box_idx]
        ):
          # Place the number
          board[r][c] = digit
          rows[r].add(digit)
          cols[c].add(digit)
          boxes[box_idx].add(digit)

          # Recurse to next cell
          if backtrack(r, c + 1):
            return True

          # Backtrack (undo)
          board[r][c] = "."
          rows[r].remove(digit)
          cols[c].remove(digit)
          boxes[box_idx].remove(digit)

      return False

    backtrack(0, 0)