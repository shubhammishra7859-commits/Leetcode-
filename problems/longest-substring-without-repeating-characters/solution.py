class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            # If the character is already in the window, move the left pointer
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
                
            # Update the character's latest position
            char_index[s[right]] = right
            
            # Calculate the max length of the current window
            max_length = max(max_length, right - left + 1)
            
        return max_length