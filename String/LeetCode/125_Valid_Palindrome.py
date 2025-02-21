class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filter = []
        for i in s:
            if i.isalnum():
                s_filter.append(i)
        
        s_new = "".join(s_filter).lower()

        if s_new == s_new[::-1]:
            return True
        else:
            return False