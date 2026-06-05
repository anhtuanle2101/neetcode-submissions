class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 + op2)
            elif token == "-":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)
            elif token == "*":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 * op2)
            elif token == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1 / op2))
            else:
                stack.append(int(token))

        return stack[0]