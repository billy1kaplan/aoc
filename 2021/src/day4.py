def test_data():
    raw_test = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 """
    return parse(raw_test.split('\n')[1:-1])

class Board:
    def __init__(self, data):
        self.data = data
        self.most_recent = None
        self.called = set()

    def draw(self, n):
        for r, row in enumerate(self.data):
            for c, val in enumerate(row):
                if val == n:
                    self.most_recent = n
                    self.called.add((r, c))

    def score(self):
        n = 0
        for r, row in enumerate(self.data):
            for c, val in enumerate(row):
                if (r, c) not in self.called:
                    n += val
        return n * self.most_recent

    def is_win(self):
        horizontal_wins = [set((i, j) for j in range(5)) for i in range(5)]
        vertical_wins = [set((j, i) for j in range(5)) for i in range(5)]

        winning_sets = [
            *horizontal_wins,
            *vertical_wins,
        ]

        for winning_set in winning_sets:
            if winning_set.issubset(self.called):
                return True
        return False

    def __str__(self):
        return '\n'.join([' '.join([str(n) for n in row]) for row in self.data])

def part1(draws, boards):
    for draw in draws:
        for board in boards:
            board.draw(draw)

            if board.is_win():
                return board.score()

def part2(draws, boards):
    last_score = 0
    already_won = set()

    for draw in draws:
        for i, board in enumerate(boards):
            if i in already_won:
                continue

            board.draw(draw)

            if board.is_win():
                last_score = board.score()
                already_won.add(i)

    return last_score

def parse(lines):
    draws = [int(n) for n in lines[0].split(',')]
    lines = lines[1:]

    i, boards = 0, []
    while i < len(lines):
        i += 1 # Ignore blank line

        board = []
        for _ in range(5):
            board.append([int(n) for n in lines[i].split()])
            i += 1
        boards.append(Board(board))

    return draws, boards


def main():
    with open('inputs/day4.txt', 'r') as f:
        input_data = parse(f.readlines())
        print(part1(*test_data()))
        print(f"Part 1: {part1(*input_data)}")
        print(part2(*test_data()))
        print(f"Part 2: {part2(*input_data)}")

if __name__ == '__main__':
    main()
