class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = 1
        suffix = 1
        n = len(nums)
        output = []

        for i in range(n):
            output.append(prefix)
            prefix *= nums[i]

        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output