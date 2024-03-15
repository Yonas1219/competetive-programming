class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]  # Initialize arr with the first element

        for i in range(len(encoded)):
            next_element = arr[i] ^ encoded[i]  # XOR operation 

        return arr