class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the car based on position
        n = len(position)
        cars = []
        for i in range(n):
            car = (position[i], i, speed[i])
            cars.append(car)
        
        cars.sort()

        time = [] #

        for car in cars:
            time.append( (target - car[0]) / car[2])
        
        #print(time)

        # monotonic stack
        
        stack = []
        count = n
        nextGreater = [n] * n
        for i in range(n-1, -1, -1):
            while stack and time[stack[-1]] < time[i]:
                stack.pop()
            if stack:
                nextGreater[i] = stack[-1]
            stack.append(i)
        
        #print(nextGreater)

        for i in range(n):
            if nextGreater[i] != n:
                count -= 1
        
        return count

        
