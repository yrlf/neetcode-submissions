class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        
        start = 0
        total = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                start = i+1
                total = 0
        return start
