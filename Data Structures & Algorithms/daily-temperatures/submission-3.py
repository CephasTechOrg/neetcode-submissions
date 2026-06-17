class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Pseudocode:
        # create results with all 0s
        # loop through each current day i
        # check every future day j after i
        # if future temp is warmer:
        #     store the distance j - i
        #     stop checking for this day
        # return results

        results = [0] * len(temperatures)

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    results[i] = j - i
                    break

        return results