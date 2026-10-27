class Solution:

  def isMatch(self, s: str, p: str) -> bool:
    s_idx, p_idx = 0, 0
    star_idx = -1
    match_idx = -1

    while s_idx < len(s):
      # If characters match or pattern has '?'
      if p_idx < len(p) and (p[p_idx] == s[s_idx] or p[p_idx] == "?"):
        s_idx += 1
        p_idx += 1
      # If pattern has '*', mark the position of '*' and current match in s
      elif p_idx < len(p) and p[p_idx] == "*":
        star_idx = p_idx
        match_idx = s_idx
        p_idx += 1
      # If current characters don't match, but we previously saw a '*'
      elif star_idx != -1:
        p_idx = star_idx + 1
        match_idx += 1
        s_idx = match_idx
      else:
        return False

    # Check for remaining characters in pattern
    while p_idx < len(p) and p[p_idx] == "*":
      p_idx += 1

    return p_idx == len(p)