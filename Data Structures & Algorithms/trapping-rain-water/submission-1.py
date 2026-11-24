class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        l_max = 0
        r_max = 0
        res = 0
        while l <= r:
            if l_max < r_max:
                res += max(l_max - height[l], 0)
                l_max = max(l_max, height[l])
                l += 1
            else:
                res += max(r_max - height[r], 0)
                r_max = max(height[r], r_max)
                r -= 1

        return res 
            