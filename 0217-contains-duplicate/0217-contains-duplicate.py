class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        k=set()
        if len(nums)==0:
            return False
        for i in nums:
            if i in k:
                return True
            else:
                k.add(i)
        return False