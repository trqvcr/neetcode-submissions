class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                i = 1
                while num + i in nums_set:
                    i += 1

                max_length = max(max_length, i)

        return max_length