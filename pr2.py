"""Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]". 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

"""



class Solution:
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return "[.]".join(address.split(".")) # split function will split each char and return a list

sol = Solution()
print(sol.defangIPaddr('1.2.1.1'))