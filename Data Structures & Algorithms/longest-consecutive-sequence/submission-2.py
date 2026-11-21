# We have to remember all substrings and iterate through and find the longest one later

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set()
        substrings = []
    
        for num in nums:
            nums_set.add(num)

        for num in nums:
            substring = []
            if num - 1 not in nums_set:
                i = 0
                while num + i in nums_set:
                    substring.append(num + i)
                    i += 1

            substrings.append(substring)

        max_length = 0
        for i in range(len(substrings)):
            if len(substrings[i]) > max_length:
                max_length = len(substrings[i])

        return max_length 
        
        