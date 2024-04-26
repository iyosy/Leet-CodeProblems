class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = defaultdict(int)
        for i in range(len(nums)):
            v = target-nums[i]
            if v in hash:
                return [hash[v],i]
            hash[nums[i]] = i
        