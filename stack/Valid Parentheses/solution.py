class Solution:
    pattern = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.pattern.values():
                stack.append(c)
            elif c in self.pattern:
                if len(stack) == 0 or stack.pop() != self.pattern[c]:
                    return False
        
        return len(stack) == 0
