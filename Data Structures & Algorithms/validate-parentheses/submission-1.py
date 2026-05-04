class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opener = '[{('
        closer = ']})'
        for char in s:
            if char in opener:
                stack.append(char)
            elif char in closer:
                if not stack:
                    return False
                if stack[-1] == '[' and char == ']':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                elif stack[-1] == '(' and char == ')':
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True