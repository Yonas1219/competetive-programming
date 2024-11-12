class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1 

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the left sorted half
                else:
                    left = mid + 1   # Target is in the right half
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target is in the right sorted half
                else:
                    right = mid - 1  # Target is in the left half

        return -1  
        

