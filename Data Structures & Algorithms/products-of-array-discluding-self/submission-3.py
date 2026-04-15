class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(0, n):
            left = nums[:i]
            right = nums[i+1:]
            left_product = math.prod(left)
            right_product = math.prod(right)
            result.append(left_product * right_product)
        return result