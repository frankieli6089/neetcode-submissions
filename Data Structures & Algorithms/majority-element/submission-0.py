class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1
                if (hash[nums[i]] > len(nums) / 2):
                    return nums[i]
            else:
                hash[nums[i]] = 1 
        
        for key in hash:
            if (hash[key] > len(nums) / 2):
                return key


        

