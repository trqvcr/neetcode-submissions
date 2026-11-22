class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
            
        return res