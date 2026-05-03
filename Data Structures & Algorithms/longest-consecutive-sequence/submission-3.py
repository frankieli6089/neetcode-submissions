class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        longest = 1
        for num in nums:
            if (num - 1) not in nums:
                temp_longest = 1
                num += 1
                while num in nums:
                    temp_longest += 1
                    num += 1
                    if temp_longest >= longest:
                        longest = temp_longest
        return longest