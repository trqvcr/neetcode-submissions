# We have to remember all substrings and iterate through and find the longest one later

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set()
        max_length = 0
    
        for num in nums:
            nums_set.add(num)

        for num in nums_set:
            if num - 1 not in nums_set:
                i = 0
                while num + i in nums_set:
                    i += 1
            
                max_length = max(max_length, i)

        return max_length 
        
        