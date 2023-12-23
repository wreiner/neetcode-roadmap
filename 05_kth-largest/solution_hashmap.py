class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        oc = {}

        for num in nums:
            if not num in oc:
                oc[num] = 0
            oc[num] += 1

        sorted_oc = sorted(oc.items(), key=lambda x: x[1], reverse=True)

        return [num[0] for num in sorted_oc][:k]

