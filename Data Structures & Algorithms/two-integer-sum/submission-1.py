class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice_map = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in indice_map:
                return [indice_map[difference], i]

            indice_map[num] = i

        return []
                
        