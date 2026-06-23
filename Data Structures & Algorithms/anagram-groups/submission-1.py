class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = defaultdict(list)

        for word in strs:
            cnt = [0]*26
            for c in word:
                cnt[ord(c) - ord('a')] += 1
            key = ""
            for i in range(26):
                key += "-" + str(i) + "-" + str(cnt[i]) +"-"
            
            record[key].append(word)
        
        res = []

        for key, val in record.items():
            res.append(list(val))

        return res

