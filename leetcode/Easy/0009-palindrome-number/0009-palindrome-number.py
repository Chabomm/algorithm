class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        list_x = list(str_x)
        list_x2 = list(reversed(list_x))
        return list_x2 == list_x