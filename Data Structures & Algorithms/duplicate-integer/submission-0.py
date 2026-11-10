class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index, x in enumerate(nums):
            for i, y in enumerate(nums):
                if x == y:
                    if index != i:
                        return True
        return False