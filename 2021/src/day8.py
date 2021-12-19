from itertools import permutations
from pprint import pprint

class Digit:
    mapping = [
        ('abcefg', 0), 
        ('cf', 1),
        ('acdeg', 2),
        ('acdfg', 3),
        ('bcdf', 4),
        ('abdfg', 5),
        ('abdefg', 6),
        ('acf', 7),
        ('abcdefg', 8),
        ('abcdfg', 9)
    ]

    @staticmethod
    def mappings_by_length(n):
        return [k for k, _ in Digit.mapping if len(k) == n]

    @staticmethod
    def display_to_digit(key):
        return { k: v for k, v in Digit.mapping }.get(key)

    @staticmethod
    def digit_to_display(key):
        return { v: k for k, v in Digit.mapping }.get(key)

def parse(lines):
    def parse_line(line):
        input_segment, output_segment = line.split(' | ')
        inputs, outputs = input_segment.split(), output_segment.split()

        return [inputs, outputs]

    return list(map(parse_line, lines))

def part1(signals):
    unique_outputs_count = 0

    for _, outputs in signals:
        for output in outputs:
            if len(output) in [2, 3, 4, 7]:
                unique_outputs_count += 1

    return unique_outputs_count

def part2(signals):
    total = 0
    for inputs, outputs in signals:
        # Mappings from signal in the input to original
        candidates = 'abcdefg'
        candidate_mappings = { k: set() for k in range(0, 10) }
        known_mappings = { k: None for k in range(0, 10) }

        for value in (inputs + outputs):
            candidates = Digit.mappings_by_length(len(value))

            if len(value) in [2, 3, 4, 7]:
                n = Digit.display_to_digit(Digit.mappings_by_length(len(value))[0])
                known_mappings[n] = set(value)

            for mapping in candidates:
                candidate_mappings[Digit.display_to_digit(mapping)].add(''.join(list(sorted(value))))

        four_and_seven = known_mappings[4].union(known_mappings[7])
        for candidate in candidate_mappings[9]:
            if len(set(candidate) - four_and_seven) == 1:
                known_mappings[9] = set(candidate)

        for candidate in candidate_mappings[0]:
            s = set(candidate)

            if not s == known_mappings[9] and known_mappings[1].issubset(s):
                known_mappings[0] = s

        for candidate in candidate_mappings[6]:
            s = set(candidate)

            if not s == known_mappings[0] and not s == known_mappings[9]:
                known_mappings[6] = s

        for candidate in candidate_mappings[3]:
            s = set(candidate)

            if known_mappings[1].issubset(s):
                known_mappings[3] = s

        f_segment = known_mappings[1] - known_mappings[6] 

        for candidate in candidate_mappings[5]:
            s = set(candidate)

            if not s == known_mappings[3] and not f_segment.issubset(s):
                known_mappings[5] = s

        for candidate in candidate_mappings[2]:
            s = set(candidate)

            if not s == known_mappings[3] and not s == known_mappings[5]:
                known_mappings[2] = s

        res = ''
        for output in outputs:
            for k, v in known_mappings.items():
                if set(output) == v:
                    res += str(k)
        total += int(res)
        print(int(res))


    print(total)
    return total

def main():
    with open('inputs/day8-test.txt', 'r') as test_file, open('inputs/day8.txt', 'r') as input_file:
        test_data = parse(test_file.readlines())
        input_data = parse(input_file.readlines())

        assert part1(test_data) == 26
        print(f"Part 1: {part1(input_data)}")

        assert part2(test_data) == 61229
        print(f"Part 2: {part2(input_data)}")

if __name__ == '__main__':
    main()
