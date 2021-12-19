from collections import deque
from pprint import pprint

class Board:
    def __init__(self, board):
        self.board = board

    def set_height(self, row, col, height):
        self.board[row][col] = height

    def adjacent_points(self, r, c):
        return [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

    def adjacent_heights(self, r, c):
        return [self.get_height(x, y) for x, y in self.adjacent_points(r, c)]

    # Out of bounds is a very large height
    # We know that 9 is the maximum height and can serve as a boundry
    def get_height(self, row, col):
        if not (0 <= row < self.rows()) or not (0 <= col < self.cols()):
            return 9
        
        return self.board[row][col]

    def rows(self):
        return len(self.board)
    
    # Assumes all rows have same number of cols.
    # Assumes that there's at least 1 row.
    def cols(self):
        return len(self.board[0])

def parse(lines):
    rows = []

    for line in lines:
        heights = list(map(int, list(line.strip())))
        rows.append(heights)

    return Board(rows)

def part1(board):
    low_heights = []
    for r in range(board.rows()):
        for c in range(board.cols()):
            height = board.get_height(r, c)

            if height < min(board.adjacent_heights(r, c)):
                low_heights.append(height)

    # Need to add 1 to each low_height per description
    return sum(low_heights) + len(low_heights)

def part2(board):
    seen = set()

    def dfs(r, c) -> int:
        if (r, c) in seen:
            return 0

        seen.add((r, c))
        height = board.get_height(r, c)

        if height < 9:
            return sum([dfs(x, y) for x, y in board.adjacent_points(r, c)]) + 1
        return 0


    # Find the center point of all basins
    basins = []
    for r in range(board.rows()):
        for c in range(board.cols()):
            height = board.get_height(r, c)

            if height < min(board.adjacent_heights(r, c)):
                basins.append((r, c))

    # Expand every basin and get its size
    basin_sizes = []
    for r, c in basins:
        basin_sizes.append(dfs(r, c))

    product = 1
    for size in sorted(basin_sizes)[-3:]:
        product *= size

    return product

def main():
    with open('inputs/day9-test.txt', 'r') as test_file, open('inputs/day9.txt', 'r') as input_file:
        test_data = parse(test_file.readlines())
        input_data = parse(input_file.readlines())

        assert part1(test_data) == 15
        print(f"Part 1: {part1(input_data)}")

        assert part2(test_data) == 1134
        print(f"Part 2: {part2(input_data)}")

if __name__ == '__main__':
    main()
