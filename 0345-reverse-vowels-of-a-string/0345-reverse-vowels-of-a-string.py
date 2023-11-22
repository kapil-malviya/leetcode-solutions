class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        vowels = set("aeiouAEIOU")
        s = list(s)
        vowel_list = [char for char in s if char in vowels]
        vowel_list.reverse()

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowel_list.pop(0)

        return ''.join(s)
        '''
        
        vowels = set("aeiouAEIOU")
        s = list(s)
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1

            # Swap the vowels
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return ''.join(s)