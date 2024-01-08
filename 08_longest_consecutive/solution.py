class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0

        if len(nums) == 1:
            return 1

        numdict = {nums[i]: 0 for i in range(len(nums))}
        print(numdict)

        if len(numdict) == 1:
            return 1
        
        j = 0
        for val in numdict:
            streak_length = 0

            # check if at lowest end of streak
            if val-1 in numdict:
                # not the lowest end so we can continue
                continue

            for j in range(val, val+len(nums)+1):
                if not j in numdict:
                    length = max(length, streak_length)
                    break

                streak_length += 1

        return length

