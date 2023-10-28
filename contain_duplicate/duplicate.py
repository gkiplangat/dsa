class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        checkdup = set()

        for x in nums:
            if x in checkdup:
                return True
            else:
                checkdup.add(x)
        return False
