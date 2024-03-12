class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if type(a and b) == str:
            return bin(int(a, 2) + int(b, 2))[2:]
        return bin(a+b)
        
        