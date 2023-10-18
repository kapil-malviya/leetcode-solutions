class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        # if ch is not found, return original string
        if ch not in word:
            return word
        
        i = 0
        j = word.index(ch)
        
        while i < j :
            word_list = list(word)
            word_list[i], word_list[j] = word_list[j], word_list[i]
            word = ''.join(word_list)
            
            i += 1
            j -= 1
            
        return word