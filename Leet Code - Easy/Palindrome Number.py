# # Approach
# return False If x is less than 0, the method will immediately return False, indicating that the number is not a palindrome. This is because negative numbers cannot be palindromes.
# return str(x) == str(x)[::-1] This line is checking if the string representation of x is equal to its reverse. Here's how it works:
# str(x) converts the number x to a string.
# str(x)[::-1] gets the characters of the string in reverse order. The [::-1] is a slice that steps backward through the entire string.
# str(x) == str(x)[::-1] checks if the original string is equal to its reverse. If it is, then the number is a palindrome, and the method returns True. Otherwise, it returns False.
# # Code
# ```
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]
# ```