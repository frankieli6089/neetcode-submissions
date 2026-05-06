class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        res = []
        for i in range(size):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            p1 = i + 1
            p2 = size - 1
            while p1 < p2:
                if nums[p1] + nums[p2] < -nums[i]:
                    p1+=1
                elif nums[p1] + nums[p2] > -nums[i]:
                    p2-=1
                else:
                    res.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1

                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1

        return res



