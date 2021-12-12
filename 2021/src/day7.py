import math

def parse(text):
    return list(map(int, text.split(',')))

def median(items):
    items = sorted(items)

    midpoint = len(items) // 2
    if len(items) % 2 == 1:
        return items[midpoint]
    else:
        return round((items[midpoint - 1] + items[midpoint]) / 2)

# TODO: Why is it not the rounded average?
#       Based on my intuition, shouldn't rounding produce the best scenario?
#       When is that not true?

# This worked for the provided test input (rounding), but was the floor for the actual input
def averages(items):
    a = sum(items) / len(items)

    return [math.floor(a), math.ceil(a)]

def natural_sum(n):
    return n * (n + 1) // 2

def part1(positions):
    m = median(positions)

    return sum([abs(position - m) for position in positions])

def part2(positions):
    ans = float('inf')
    for fuel_position in averages(positions):
        ans = min(ans, sum([natural_sum(abs(position - fuel_position)) for position in positions]))
    return ans

def main():
    with open('inputs/day7-test.txt', 'r') as test_file, open('inputs/day7.txt', 'r') as input_file:
        test_data = parse(test_file.read())
        input_data = parse(input_file.read())

        assert part1(test_data) == 37
        print(f"Part 1: {part1(input_data)}")

        assert part2(test_data) == 168
        print(f"Part 2: {part2(input_data)}")

if __name__ == '__main__':
    main()
