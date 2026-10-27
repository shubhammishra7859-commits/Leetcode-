class Solution:

  def multiply(self, num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
      return "0"

    m, n = len(num1), len(num2)
    res = [0] * (m + n)

    # Multiply each digit from right to left
    for i in range(m - 1, -1, -1):
      for j in range(n - 1, -1, -1):
        digit1 = ord(num1[i]) - ord("0")
        digit2 = ord(num2[j]) - ord("0")

        product = digit1 * digit2
        p1, p2 = i + j, i + j + 1

        # Add product to the existing value at p2
        total = product + res[p2]

        # Update res[p2] with the single digit and res[p1] with the carry
        res[p2] = total % 10
        res[p1] += total // 10

    # Convert array to string and remove leading zeros
    result_str = "".join(map(str, res))
    return result_str.lstrip("0")