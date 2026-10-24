class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findBound(isFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1  # Keep searching on the left
                    else:
                        left = mid + 1   # Keep searching on the right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        first_pos = findBound(isFirst=True)
        
        # If target doesn't exist, no need to search for the last position
        if first_pos == -1:
            return [-1, -1]
            
        last_pos = findBound(isFirst=False)
        
        return [first_pos, last_pos]