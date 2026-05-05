class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, curr in enumerate(nums,1):
            for j, item in enumerate(nums[i:],1):
                if item + curr == target:
                    return [i-1, i+j-1]
        return []