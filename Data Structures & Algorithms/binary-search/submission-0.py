class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        low = 0
        high = size - 1

        while low <= high:
            mid = ((high - low)// 2) + low
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] == target:
                return mid
        
        else:
            return -1