class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer  = []
        for i in range(len(nums)):
            ans = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    ans += 1
            answer.append(ans)
        return answer