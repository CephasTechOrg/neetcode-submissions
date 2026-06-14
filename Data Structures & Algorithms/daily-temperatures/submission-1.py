class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Pseudocode:
        # create res with all 0s
        # create an empty stack
        # loop through each day i
        # while stack is not empty and current temp is warmer:
        #     pop the previous waiting day
        #     store how many days it waited
        # add current day i to stack
        # return res

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev

            stack.append(i)

        return res