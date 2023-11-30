class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        result = []

        for i in range(len(words)):
            
            # nested loop to compare current word with all other words
            for j in range(len(words)):
                
                # check if words are different and if current word is a substring of any other word
                if i != j and words[i] in words[j]:
                    
                    # if match found, append current word to list
                    result.append(words[i])
                    
                    break

        return result