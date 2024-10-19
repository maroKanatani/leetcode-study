class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for i,n in enumerate(nums):
            if n in tmp:
                return [tmp[n], i]
            tmp[target - n] = i
        return []
