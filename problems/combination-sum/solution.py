class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, current_comb: List[int], rem_target: int):
            if rem_target == 0:
                result.append(list(current_comb))
                return
            if rem_target < 0:
                return
            
            for i in range(start, len(candidates)):
                # Choose the number
                current_comb.append(candidates[i])
                # Explore with the same index 'i' (since elements can be reused)
                backtrack(i, current_comb, rem_target - candidates[i])
                # Unchoose the number (backtrack)
                current_comb.pop()
                
        backtrack(0, [], target)
        return result