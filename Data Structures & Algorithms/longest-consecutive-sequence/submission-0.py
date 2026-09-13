class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nmSet = set(nums)
        for n in nmSet:
            if (n-1) not in nmSet:
                length = 1
                while (n+length) in nmSet:
                    length+=1
                longest = max(length,longest)
        return longest