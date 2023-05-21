class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
       
        n = len(nums)
        val = 0
        for i in range(0, n):
            nums[i] = n * ( nums[nums[i]] % n) + nums[i]
        for i in range(0,n):
            nums[i] = nums[i] // n
        return nums