class Solution(object):
    def isPowerOfTwo(n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        return (n &(n-1))==0 
n=int(input("Enter a number: "))
print(Solution.isPowerOfTwo(n))