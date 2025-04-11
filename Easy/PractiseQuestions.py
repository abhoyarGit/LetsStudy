#Move Zeroes
#
#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.
#
#Example 1:
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]

def moveZeroes(nums):
    # move all non zero to right
    # dont do anything if zero is there
    # swap when u get non zero number
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            j += 1

    print(nums)

#moveZeroes([1,0,1,1,0,0,0,0,2,2])

def removeDuplicate(nums):
    i = 0
    j = 0
    while (j < len(nums)):
        if nums[i] == nums[j]:
            j = j + 1
        else:
            i = i + 1
            nums[i] = nums[j]

        print("#",nums)

#removeDuplicate([1,1,2,2,3,3])


#House Rob
#https://www.youtube.com/watch?v=VXqUQYGMnQg
# Space-complexity: O(1)
class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(first + nums[i], second)
            first = second
            second = curr
        return curr
