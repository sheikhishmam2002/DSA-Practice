class Solution:
    def reverseWords(self, s: str) -> str:
        #space-free
        words = " ".join(s.split())
        word_list = list(words.split())

        # reversing
        word_list_reverse = word_list[::-1]

        result = " ".join(word_list_reverse)
        return result