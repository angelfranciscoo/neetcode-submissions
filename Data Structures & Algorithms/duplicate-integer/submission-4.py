# Brute Force
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         i = 0
#         for i in range(len(nums)):
#             for k in range(i+1, len(nums)):
#                 if(nums[i] == nums[k]):
#                     return True
#         return False

# Linear Scan
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         _ = nums
#         for i in range(len(nums) - 1):
#             if(nums[i] == _[i+1]):
#                 return True

#         return False

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _ = set()
        for i in nums:
            if i in _:
                return True
            _.add(i)
        return False

