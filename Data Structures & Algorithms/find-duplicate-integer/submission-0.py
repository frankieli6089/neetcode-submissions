class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_ptr = nums[0]
        fast_ptr = nums[0]
        while True:
            
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[nums[fast_ptr]]

            if slow_ptr == fast_ptr:
                break
        
        slow = nums[0]
        while slow != fast_ptr:
            slow = nums[slow]
            fast_ptr = nums[fast_ptr]
        return slow
            