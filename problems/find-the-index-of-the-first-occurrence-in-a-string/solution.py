class Solution:

  def strStr(self, haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)

    # If needle is longer than haystack, it can't be a substring
    if m > n:
      return -1

    # Slide the window across haystack
    for i in range(n - m + 1):
      if haystack[i : i + m] == needle:
        return i

    return -1