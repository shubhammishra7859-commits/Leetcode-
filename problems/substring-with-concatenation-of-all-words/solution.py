from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        if s_len < total_len:
            return []
        
        word_count = Counter(words)
        result = []
        
        # Iterate over each possible offset
        for i in range(word_len):
            left = i
            right = i
            seen_words = Counter()
            count = 0
            
            while right + word_len <= s_len:
                # Extract the next word of length word_len
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    seen_words[word] += 1
                    count += 1
                    
                    # If the word appears more times than allowed, shrink from the left
                    while seen_words[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen_words[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # If we matched all words, record the starting index
                    if count == num_words:
                        result.append(left)
                else:
                    # Not a valid word, reset the window
                    seen_words.clear()
                    count = 0
                    left = right
                    
        return result