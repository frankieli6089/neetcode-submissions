class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_set = set(['+', '-', '/', '*'])

        for token in tokens:
            print(stack)
            if token not in operator_set:
                stack.append(int(token))
            else:
                if token == '+':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                    stack.append(operand2 + operand1)
                elif token == '-':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                    stack.append(operand2 - operand1)
                elif token == '*':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                    stack.append(operand2 * operand1)
                elif token == '/':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                    stack.append(int(operand2 / operand1))
                
        return stack[0]

