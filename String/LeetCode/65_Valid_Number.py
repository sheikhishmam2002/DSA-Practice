import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Regular expression to match a valid number
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        return bool(re.match(pattern, s.strip())) # Strip leading/trailing space and match the pattern
        