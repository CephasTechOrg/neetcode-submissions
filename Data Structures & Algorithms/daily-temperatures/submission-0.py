class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        results = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(1 + i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    results[i] = j - i
                    break
                else:
                    results[i] = 0
        return results            


