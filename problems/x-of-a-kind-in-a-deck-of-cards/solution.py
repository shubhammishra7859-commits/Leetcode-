import math
from collections import Counter
from typing import List


class Solution:

  def hasGroupsSizeX(self, deck: List[int]) -> bool:
    counts = Counter(deck).values()

    # Calculate GCD of all counts
    common_gcd = 0
    for count in counts:
      common_gcd = math.gcd(common_gcd, count)

    return common_gcd >= 2