def mergeAlternately(self, word1: str, word2: str) -> str:
        maxlen = max(len(word1), len(word2))
        result = ""
        
        for i in range(maxlen):
            result += word1[i] if i < len(word1) else ""
            result += word2[i] if i < len(word2) else ""
            
        return result
