class Solution:
    def isValid(self, s: str) -> bool:
        opens = ["(", "{", "["]
        closes = [")", "}", "]"]

        stack = []

        for c in s:
            if not stack:
                if c in closes:
                    return False
                stack.append(c)
            elif c in opens:
                stack.append(c)
            elif (stack[-1] == "(" and c == ")") or (stack[-1] == "{" and c == "}") or (stack[-1] == "[" and c == "]"):
                stack.pop()
            else:
                return False

        return len(stack) == 0

            