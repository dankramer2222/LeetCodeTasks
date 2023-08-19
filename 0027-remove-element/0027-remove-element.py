class Solution:
    def removeElement(self, nums, val):
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        
        return slow

# Test the implementation with the provided example
nums = [3, 2, 2, 3]
val = 3
expectedNums = [2, 2]
expectedLength = len(expectedNums)

# Create an instance of the Solution class
solution = Solution()

k = solution.removeElement(nums, val)
assert k == expectedLength

# Sort the first k elements of nums
nums.sort()
for i in range(expectedLength):
    assert nums[i] == expectedNums[i]

