class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""

        for s in strs:
            n = len(s)
            res+= str(n) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:

        start = 0
        end = 0
        n = len(s)
        res = []
        print(s)

        while end < n:
            size = 0

            while s[end] != '#':
                #print(s[end])
                size = size * 10 + int(s[end])
                end += 1
            
            # i = #
            end += 1
            if size > 0:
                seg = s[end: end + size]
                #print(seg)
                
            else:
                seg = ""
            res.append(seg)
            end = end + size
        return res

