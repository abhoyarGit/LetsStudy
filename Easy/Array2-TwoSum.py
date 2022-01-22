# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#  Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(0,len(nums)):
#             j = target - nums[i]

#             if j in nums[i+1:len(nums)]:
#                 #return [i,nums.index(j)]
#                 return [i,i+1+(nums[i+1:len(nums)].index(j))]


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dic = {}
#         for i in range(len(nums)):
#             if nums[i] in dic: return [i,dic[nums[i]]]
#             dic[target - nums[i]] = i
#             print(dic)