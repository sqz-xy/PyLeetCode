class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for idx, i in enumerate(nums):
            for jdx, j in enumerate(nums):
                if jdx == idx:
                    continue
                if i + j == target:
                    return [idx, jdx]