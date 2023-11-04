class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        # Calculate the maximum time for ants moving to the left
        max_left_time = max(left) if left else 0

        # Calculate the maximum time for ants moving to the right
        max_right_time = n - min(right) if right else 0

        # The last ant(s) to fall off the plank will be the one that takes the maximum time
        return max(max_left_time, max_right_time)

# Create an instance of the Solution class
solution = Solution()

# Define the inputs
n = 4
left = [4, 3]
right = [0, 1]

# Call the getLastMoment method to find the moment when the last ant(s) fall out of the plank
result = solution.getLastMoment(n, left, right)

# Print the result
print(result)
