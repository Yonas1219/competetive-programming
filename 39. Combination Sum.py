class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], result)
        return result
    def backtrack(self, candidates, target, index, path, result):
        if target == 0:
            result.append(path)
            return 
        for i in range(index, len(candidates)):
            if candidates[i] <= target:
                self.backtrack(candidates, target-candidates[i], i, path+[candidates[i]], result)