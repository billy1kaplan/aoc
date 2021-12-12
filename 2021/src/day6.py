from collections import Counter

def parse(text):
    return list(map(int, text.split(',')))

def advance(state):
    new_state = Counter()

    for day, count in state.items():
        if day == 0:
            new_state[6] += count
            new_state[8] += count
        else:
            new_state[day - 1] += count

    return new_state

def simulate(initial, n_days):
    state = Counter(initial)

    for _ in range(n_days):
        state = advance(state)

    return sum(state.values())


def part1(initial):
    return simulate(initial, 80)

def part2(initial):
    return simulate(initial, 256)

def main():
    with open('inputs/day6-test.txt', 'r') as test_file, open('inputs/day6.txt', 'r') as input_file:
        test_data = parse(test_file.read())
        input_data = parse(input_file.read())

        assert part1(test_data) == 5934
        print(f"Part 1: {part1(input_data)}")

        assert part2(test_data) == 26984457539
        print(f"Part 2: {part2(input_data)}")

if __name__ == '__main__':
    main()
