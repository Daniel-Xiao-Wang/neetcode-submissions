class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {"}": "{", "]": "[", ")": "("}

        for i in s:
            if i in char_map:
                if stack and stack[-1] == char_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False
