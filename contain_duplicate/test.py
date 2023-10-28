from duplicate import Solution
# Create an instance of the duplicate class
duplicate = Solution()

# Test cases
nums1 = [1, 2, 3, 4, 5]  # No duplicates, should return False
nums2 = [1, 2, 3, 1, 4, 5]  # Contains duplicate (1), should return True
nums3 = []  # Empty list, should return False
nums4 = [1]  # Single element, should return False
nums5 = [1, 1, 1, 1, 1]  # All elements are the same, should return True
nums6 = [1, 2, 3, 4, 5, 6]  # No duplicates, should return False

# Test the containsDuplicate method
result1 = duplicate.containsDuplicate(nums1)
result2 = duplicate.containsDuplicate(nums2)
result3 = duplicate.containsDuplicate(nums3)
result4 = duplicate.containsDuplicate(nums4)
result5 = duplicate.containsDuplicate(nums5)
result6 = duplicate.containsDuplicate(nums6)

# Print the results
print("Result for nums1:", result1)  # Should print "False"
print("Result for nums2:", result2)  # Should print "True"
print("Result for nums3:", result3)  # Should print "False"
print("Result for nums4:", result4)  # Should print "False"
print("Result for nums5:", result5)  # Should print "True"
print("Result for nums6:", result6)  # Should print "False"
