class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            tem = temperatures[i]
            count = 0
            exist = False
            for j in range(i + 1, len(temperatures)):
                count += 1
                if temperatures[j] > tem:
                    exist = True
                    break
            result.append(count if exist else 0)
                
        return result