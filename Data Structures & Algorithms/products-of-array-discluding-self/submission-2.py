# Iterate over index
# Solve in O(n)
# Say we have [0, 0, 1, 0] product = 0
# We want [product, product, product, product]
# Say we have [1, 0, 1, 2] product = 0
# We want [0, product, 0, 0]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1;
        output = []
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num

        if zero_count > 1:
            return [0 for num in nums]

        elif zero_count == 1:
            for num in nums:
                if num != 0:
                    output.append(0)
                else:
                    output.append(product)

        else: 
            for num in nums:
                output.append(product//num)
        
        return output