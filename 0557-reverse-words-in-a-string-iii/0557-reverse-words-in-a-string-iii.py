class Solution:
    def reverseWords(self, s: str) -> str:
        
        # initialize an empty list to store words
        words = []
        
        start = 0
        end = 0
        
        # iterate through each character in string
        for i in range(len(s)):
            if s[i] == ' ':
                # when space is there it means end of word
                end = i
                
                # extract word and add it to list
                word = s[start:end]
                words.append(word)
                
                # update start index for next word
                start = i + 1
                
        words.append(s[start:])
        
        reversed_words = []
        
        for word in words :
            reversed_word = ''
            for char in word:
                reversed_word = char + reversed_word
            reversed_words.append(reversed_word)
            
        result = ' '.join(reversed_words)
        
        return result