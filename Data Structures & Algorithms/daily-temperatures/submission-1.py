class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack1 = []
        stack2 = []
        result = []
        for i in range(len(temperatures)):
            count = 0
            num = temperatures.pop()
            if stack1:
                while stack1 and num >= stack1[-1]:
                    count += stack2.pop()
                    stack1.pop()
                if stack1:
                    count += 1
                else:
                    count = 0
                stack2.append(count)
                stack1.append(num)
                result.append(count)
            else:
                stack2.append(0)
                stack1.append(num)
                result.append(0)

        result.reverse()
        return result