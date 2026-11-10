class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Solution 1:
        # for index, x in enumerate(nums):
        #     for i, y in enumerate(nums):
        #         if x == y:
        #             if index != i:
        #                 return True
        # return False
        # Solution 2:
        # checklist = []
        # for n in nums:
        #     if n in checklist:
        #         return True
        #     checklist.append(n)
        # return False
        # Solution 3: the same as solution 2
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

