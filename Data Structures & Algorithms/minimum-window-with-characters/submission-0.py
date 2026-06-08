class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 22:13 -> 22:23 
        # O(N + M), O(N)
        target = Counter(t) # {a:2, b:1}  
        window = {} # {a:1, } valid = len(target)
        valid = 0 
        n = len(s)

        l, r = 0, 0
        # 
        # [OUZODYXAZ V 
        #         ] -> OUZODYX , valid = 3 = len(target)
        #   [              UZODYX , valid = 3  ->  r - l
        #    [              ZODYX , valid = 3  ->  r - l
        #     [              ODYX , valid = 2 
        #     [              ODYXA , valid = 2 
        #     [              ODYXAZ , valid = 3 
       
        ans = ""
        length = float('inf')
        while (r < n):
            c = s[r]
            r += 1

            if c not in window:
                window[c] = 0
            window[c] += 1

            if c in target and window[c] == target[c]:
                valid += 1

            while (l < r and valid == len(target)):
                # update results
                if r - l < length:

                    length = min(length, r - l)
                    ans = s[l:r]
                

                d = s[l]
                if d in target and window[d] == target[d]: # {a:2} -> {a:1}
                    valid -= 1

                window[d] -= 1
                
                if window[d] == 0:
                    del(window[d])

                l += 1

        return ans