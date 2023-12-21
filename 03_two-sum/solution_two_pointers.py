class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return None

        for fidx, forward in enumerate(nums):
            for bidx in range(len(nums)-1, -1, -1):
                if bidx <= fidx:
                    break

                backward = nums[bidx]

                if forward + backward == target:
                    return [fidx, bidx]
        
        return None

