class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_num = [(num, i) for i, num in enumerate(nums)]
        index_num.sort()
        l, r = 0, len(index_num)-1
        while l<r:
            currentsum = index_num[l][0] + index_num[r][0]
            if currentsum > target:
                r -= 1
            elif currentsum < target:
                l += 1
            elif currentsum == target:
                return sorted([index_num[l][1], index_num[r][1]])
        return []