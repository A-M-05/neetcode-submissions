class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(0, n):
            num = nums[i]
            if num == 0:
                product = math.prod(nums[:i] + nums[i+1:])
                result.append(product)
            else:
                product = math.prod(nums[:i] + nums[i+1:])
                result.append(product)
        return result