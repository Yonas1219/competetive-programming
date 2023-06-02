class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value  # Store the value at the correct index
        chunk = []
        
        # Check if the next value in order is available
        while self.pointer < len(self.stream) and self.stream[self.pointer]:
            chunk.append(self.stream[self.pointer])
            self.pointer += 1

        return chunk


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)