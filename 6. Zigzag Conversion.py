class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char

            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            current_row += 1 if going_down else -1

        return ''.join(rows)

# Example usage:
solution = Solution()
input_str = "PAYPALISHIRING"
num_rows = 3
result = solution.convert(input_str, num_rows)
print(result)
