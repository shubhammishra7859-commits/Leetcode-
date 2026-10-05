class Solution:
    def threeSum(self, nums: list[int]) -> list[int]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # If the anchor element is greater than 0, remaining elements will also be > 0
            if nums[i] > 0:
                break

            # Skip duplicate anchor values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate values for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res