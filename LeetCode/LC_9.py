#Om Namah Shivaya
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x>0:
            x = str(x)
            if x == x[::-1]:
                return True
            else:
                return False
        else:
            return False