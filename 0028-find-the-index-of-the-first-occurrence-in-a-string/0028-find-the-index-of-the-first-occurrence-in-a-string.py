class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle)   # returns -1 if substring not found
        return index