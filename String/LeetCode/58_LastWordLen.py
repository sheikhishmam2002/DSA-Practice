class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        non_space_str = " ".join(s.split())
        str_list = list(non_space_str.split(" "))
        return len(str_list[-1])