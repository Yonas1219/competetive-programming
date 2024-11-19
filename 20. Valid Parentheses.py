class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in brackets_map:
                first_element = stack.pop() if stack else '#'
                if brackets_map[char] != first_element:
                    return False
            else:
                stack.append(char)
        return not stack    

