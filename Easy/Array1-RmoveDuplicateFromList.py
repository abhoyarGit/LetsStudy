# Python3 program to
# remove duplicates
# Function to remove
# duplicate elements

# This function returns
# new size of modified
# array.
#// If the current element is equal to the next element, we skip.
# Two pointer approach

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[i] == nums[j]:
                j = j + 1
            else:
                i = i + 1
                nums[i] = nums[j]
        print(nums[0:i + 1])
        return i + 1


a = Solution()
a.removeDuplicates([1, 1, 2])
