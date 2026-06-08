class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #22:19
        # find (4, 0,0) ->k in total, compare k//2 from each list 
        # find(3, starting idx of nums1 1, starting idx of nums2 0) ->  check 3//2 from nums1, 3 - 3//2 from nums2
        # find(2, 3, 0) 
        # find(1, 4, 0)
        # [x,x,x,x,5] 
        # [8,9]

        # [x,x,] 
        # [7,8,9, 10, 11]  fink(k=3) -> k1 =1, k2 = 3-1 =2, compare k1 and k2    fink(k=2, 1, 0) k1 = 2//2 = 1, k2 = 2-1 =1  -> find()
        # M+N=1000 -> find (500) discard 250 from either nums1 or nums2 -> find(250) -> discard 125 -> find(125)
        # 500 -> 250 -> 125 -> log(M+N)
        # k = (m+n)//2, (m+n)//2-1
        # O(log(K)) <= O(log(m+n))
        # k < (m+n)
        # O(log(max(m,n)))        

        # [1,2,3, 4, 5, 6, 7,8,9,10,11] ->   
        #        s1          e1
        # [1, 3, [5], 7 , 9, 11] -> m
        # s2             e2
        # [2, 4, [6], 8, 10] -> n 

        # find (6, 0, 0) -> find (4, 2, 0) -> find(1, s1, s2) -> return min(nums[s1], nums[s2])
        
        # Target: to find the (m+n)//2 th number in merged list

        # -> define a function find the Kth largest number from nums1 and nums2 
        # -> if n+m is odd: findK(6) , or if it is even: (findK(6)+findK(7))/2
        # -> check (3) in nums1, and check (3) in nums2 and compare, the smaller one can be excluded 


        def findK(k, s1, s2):

            if s1 > m-1:
                return nums2[s2+k-1]
            if s2 > n-1:
                return nums1[s1+k-1]

            if k == 1:
                return min(nums1[s1], nums2[s2])
            k1 = k//2
            k2 = k - k1

            compare1 = nums1[s1+k1-1] if s1+k1-1 < m else float('inf') 
            compare2 = nums2[s2+k2-1] if s2+k2-1 < n else float('inf')


            if compare1 < compare2:
                return findK(k - k1, s1 + k1, s2)
            else:
                return findK(k - k2, s1, s2 + k2)


        
        m, n = len(nums1), len(nums2)
        if m < n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        mid = (m + n + 1)//2
        if (m+n) % 2 == 0:
            return (findK(mid+1, 0, 0) + findK(mid,0,0))/2
        else:
            return findK(mid, 0,0)
