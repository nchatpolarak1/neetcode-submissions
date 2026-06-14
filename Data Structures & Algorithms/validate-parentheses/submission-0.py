class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Hashmap stores parentheses
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}
        
        for c in s:
            if c in closeToOpen:
                # stack not empty, top/last value of stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else: # don't match
                    return False

            else: # ['(', '[', '{']
                stack.append(c)
        
        return True if not stack else False