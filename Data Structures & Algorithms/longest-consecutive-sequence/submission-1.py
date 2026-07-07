class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        used = set()
        record = {}

        for num in nums:
            if num in used:
                continue
            
            if num not in record:
                record[num] = 1
                j = num
                while j + 1 in nums:
                    used.add(j+1)
                    record[num] += 1
                    j += 1
        

        #print(record)
        return max(record.values()) if record else 0