class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
            
        result = 0

        for word in words:
            
            # count of each character in char string
            char_count = {}
            
            for char in chars:
                char_count[char] = char_count.get(char, 0) + 1

            # to check if current word in char string
            is_good = True
            
            for char in word:
                if char not in char_count or char_count[char] == 0:
                    is_good = False
                    break
                
                # if character is present, decrement its count
                char_count[char] -= 1

            if is_good:
                result += len(word)

        return result