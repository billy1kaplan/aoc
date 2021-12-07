from collections import Counter

class LineSegment:
    def __init__(self, start, end):
        self.start, self.end = sorted([start, end])

    def is_horizontal(self):
        _, y1 = self.start
        _, y2 = self.end

        return y1 == y2

    def is_vertical(self):
        x1, _ = self.start
        x2, _ = self.end

        return x1 == x2
    
    def points(self):
        """
        Returns a list of the points that this line segment covers
        """

        # Hack for now, this will only work for vertical/horizontal lines

        # x1 == x2
        if self.is_vertical():
            x, y1 = self.start
            _, y2 = self.end

            return [(x, y) for y in range(y1, y2 + 1)]


        if self.is_horizontal():
            x1, y = self.start
            x2, _ = self.end

            return [(x, y) for x in range(x1, x2 + 1)]

        x1, y1 = self.start
        x2, y2 = self.end

        if y2 > y1:
            return [(x1 + i, y1 + i) for i in range(y2 - y1 + 1)]
        else:
            return [(x1 + i, y1 - i) for i in range(y1 - y2 + 1)]


    def __str__(self):
        return f"{self.start} -> {self.end}"

def display_counts(cover_counts):
    max_x, max_y = 0, 0
    for x, y in cover_counts.keys():
        max_x, max_y = max(x, max_x), max(y, max_y)

    print(max_x, max_y)
    for i in range(max_y + 1):
        line = []

        for j in range(max_x + 1):
            count = cover_counts[(j, i)]

            if count == 0:
                line.append('.')
            else:
                line.append(str(count))

        print(''.join(line))


def part1(line_segments):
    cover_counts = Counter()

    for line_segment in line_segments:
        if line_segment.is_horizontal() or line_segment.is_vertical():
            cover_counts.update(line_segment.points())

    # print(display_counts(cover_counts))
    return len([count for count in cover_counts.values() if count >= 2])

def part2(line_segments):
    cover_counts = Counter()

    for line_segment in line_segments:
        cover_counts.update(line_segment.points())

    # print(display_counts(cover_counts))
    return len([count for count in cover_counts.values() if count >= 2])

def parse(lines):
    line_segments = []
    for line in lines:
        start, end = line.split(' -> ', 2)
        x1, y1 = start.split(',', 2)
        x2, y2 = end.split(',', 2)

        line_segments.append(LineSegment((int(x1), int(y1)), (int(x2), int(y2))))

    return line_segments

def main():
    with open('inputs/day5-test.txt', 'r') as test_file, open('inputs/day5.txt', 'r') as input_file:
        test_line_segments = parse(test_file)
        line_segments = parse(input_file)

        assert part1(test_line_segments) == 5
        print(f"Part 1: {part1(line_segments)}")

        assert part2(test_line_segments) == 12
        print(f"Part 2: {part2(line_segments)}")

if __name__ == '__main__':
    main()
