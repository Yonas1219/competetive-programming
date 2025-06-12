class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, used, res):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                # Skip used elements
                if used[i]:
                    continue
                # Skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                # Choose
                used[i] = True
                path.append(nums[i])
                # Explore
                backtrack(path, used, res)
                # Un-choose
                path.pop()
                used[i] = False

        nums.sort()  # Sort to handle duplicates
        res = []
        used = [False] * len(nums)
        backtrack([], used, res)
        return res
