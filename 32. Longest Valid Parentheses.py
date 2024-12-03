class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # -1 to handle edge cases
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push index of '(' to the stack
            else:
                stack.pop()  # Pop the top element for matching ')'
                
                if not stack:
                    stack.append(i)  # If stack is empty, push the index of ')'
                else:
                    max_length = max(max_length, i - stack[-1])  # Calculate the length of the current valid substring
        
        return max_length
