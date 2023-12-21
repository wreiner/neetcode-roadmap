class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        parts = {}

        for idx, num in enumerate(nums):
            if num in parts:
                return [parts[num], idx]

            parts[target - num] = idx

