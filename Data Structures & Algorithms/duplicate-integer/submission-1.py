class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            l,r = l + 1, r+1
        return False