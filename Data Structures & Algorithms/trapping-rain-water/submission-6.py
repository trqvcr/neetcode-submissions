class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        l_max = height[l]
        r_max = height[r]
        res = 0
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += max(l_max - height[l], 0)
            else:
                r -= 1
                r_max = max(height[r], r_max)
                res += max(r_max - height[r], 0)

        return res 
            