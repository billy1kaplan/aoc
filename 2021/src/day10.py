def parse(lines):
    return [line.strip() for line in lines]

def score(ch):
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    return scores[ch]

def score_part2(ch):
    scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    return scores[ch]


def check(line):
    stack = []

    mapping = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }

    for ch in line:
        if ch in '([{<':
            stack.append(ch)
        else:
            if not stack[-1] == mapping[ch]:
                return ch
            else:
                stack.pop()

def completion(line):
    stack = []

    mapping = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }

    for ch in line:
        if ch in '([{<':
            stack.append(ch)
        else:
            stack.pop()

    s = ''
    while stack:
        cur = stack.pop()

        s += mapping[cur]
    return s

def part1(lines):
    total = 0
    for line in lines:
        found = check(line)

        if found:
            total += score(found)

    return total

def part2(lines):
    scores = []
    for line in lines:
        if not check(line):
            s = completion(line)

            total = 0
            for ch in s:
                total *= 5
                total += score_part2(ch)
            scores.append(total)

    return list(sorted(scores))[len(scores) // 2]


def main():
    with open('inputs/day10-test.txt', 'r') as test_file, open('inputs/day10.txt', 'r') as input_file:
        test_data = parse(test_file.readlines())
        input_data = parse(input_file.readlines())

        assert part1(test_data) == 26397
        print(f"Part 1: {part1(input_data)}")

        assert part2(test_data) == 288957
        print(f"Part 2: {part2(input_data)}")

if __name__ == '__main__':
    main()
