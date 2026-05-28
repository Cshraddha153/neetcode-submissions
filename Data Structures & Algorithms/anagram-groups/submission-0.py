class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord('a')] += 1 
            count = tuple(count)
            dict1[count].append(word)
        print(dict1.values())
        return dict1.values()