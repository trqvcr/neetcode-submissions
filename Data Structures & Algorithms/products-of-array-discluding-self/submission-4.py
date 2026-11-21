class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = 1
        suffix = 1
        n = len(nums)
        output = []

        for i in range(n):
            output.append(prefix)
            prefix *= nums[i]

        for i in range(n):
            output[n-1-i] *= suffix
            suffix *= nums[n-i-1]

        return output