class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_list_1 = list(word1)
        word_list_2 = list(word2)
        alternate_list = list()

        for i in range(len(word1)):
            alternate_list.append(word_list_1[i])
            if i < len(word2):
                alternate_list.append(word_list_2[i])
        
        if len(word2) > len(word1):
            alternate_list.extend(word_list_2[len(word1):])
        
        merged_string = "".join(alternate_list)
        
        return merged_string
        