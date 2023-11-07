class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        # list to store the valid words
        valid_words = []
        
        for word in words:
            lower_word = word.lower()
            
            # check word that contains characters from only one row
            if set(lower_word).issubset(row1) or set(lower_word).issubset(row2) or set(lower_word).issubset(row3):
                valid_words.append(word)
                
        return valid_words