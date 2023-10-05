def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            # Sort the characters in the word to create a key
            sorted_word = ''.join(sorted(word))
            
            # Check if the sorted word is already in the dictionary, if not, add it as a key
            if sorted_word not in dic:
                dic[sorted_word] = [word]
            else:
                dic[sorted_word].append(word)
        
        # Return the values of the dictionary as the grouped anagrams
        return list(dic.values())
