import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.function.BiFunction;
import java.util.function.BiPredicate;
import java.util.stream.Collectors;

class Solution {
    public static void main(String[] args) {
        try {
            List<String> inputData = Files.readAllLines(Paths.get("inputs/day3.txt"));
            List<String> testData = List.of(
                    "00100",
                    "11110",
                    "10110",
                    "10111",
                    "10101",
                    "01111",
                    "00111",
                    "11100",
                    "10000",
                    "11001",
                    "00010",
                    "01010");

            if (part1(testData) != 198) {
                throw new Error("Test failed!");
            }

            if (part2(testData) != 230) {
                throw new Error("Test failed!");
            }

            System.out.printf("Part 1: %d", part1(inputData));
            System.out.printf("Part 2: %d", part2(inputData));
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    public static int part1(List<String> data) {
        int integerSize = data.get(0).length();
        int[] onesCount = new int[integerSize];

        for (String number : data) {
            for (int i = 0; i < number.length(); i++) {
                if (number.charAt(i) == '1') {
                    onesCount[i] += 1;
                }
            }
        }

        int gammaRate = 0;
        int total = data.size();

        for (int i = 0; i < onesCount.length; i++) {

            // Since we're looking at binary numbers, we know that all digits are
            // either 0 or 1.
            // If there are more 1's than 0's (things that are not 1's)
            if (onesCount[i] > total - onesCount[i]) {
                // We need to convert from binary into decimal
                int position = onesCount.length - 1 - i;
                gammaRate += Math.round(Math.pow(2, position));
            }
        }

        // Flips bits in the epsilon rate
        // e.g.
        // UNUSED since numbers may be < 32 bit
        // XOR 00000000000...01001
        // ... 00000000000...11111
        // ... 00000000000...10110
        // int epsilonRate = gammaRate ^ Integer.parseInt(new String(new char[integerSize]).replace("\0", "1"), 2);
        int epsilonRate = gammaRate ^ Integer.parseInt("1".repeat(integerSize), 2);

        return gammaRate * epsilonRate;
    }

    enum SelectionStrategy {
        OXYGEN_RATING,
        CARBON_DIOXIDE_RATING
    }

    // I'm not so sure this is a great strategy
    // This reminds me a lot the defunctionalization talk that Jimmy Koppel gave:
    // https://blog.sigplan.org/2019/12/30/defunctionalization-everybody-does-it-nobody-talks-about-it/
    // There are definitely other ways of doing this (and this is probably a poor
    // abstraction)
    // You could also pass in a function that takes the number of ones and zeros and
    // determines the character that must match
    // BiFunction<Integer, Integer, Character>
    // e.g. for oxygen: ... = (onesCount, zerosCount) -> onesCount >= zerosCount ?
    // '1' ? '0';
    private static int selectCandidate(List<String> data, SelectionStrategy strategy) {
        int integerSize = data.get(0).length();
        List<String> candidates = new ArrayList<>(data);

        int result = 0;

        for (int i = 0; i < integerSize; i++) {
            int onesCount = 0;
            for (String candidate : candidates) {
                if (candidate.charAt(i) == '1') {
                    onesCount += 1;
                }
            }

            int totalCount = candidates.size();
            char mustMatch;
            if (strategy == SelectionStrategy.OXYGEN_RATING) {
                mustMatch = onesCount >= totalCount - onesCount ? '1' : '0';
            } else if (strategy == SelectionStrategy.CARBON_DIOXIDE_RATING) {
                mustMatch = onesCount < totalCount - onesCount ? '1' : '0';
            } else {
                throw new Error("Must pass a supported strategy");
            }

            final int index = i;
            candidates = candidates.stream().filter((c) -> c.charAt(index) == mustMatch).collect(Collectors.toList());

            // This would fail if there was only 1 candidate from the start
            // Doesn't matter in this case
            if (candidates.size() == 1) {
                result = Integer.parseInt(candidates.get(0), 2);
                break;
            }
        }

        return result;
    }

    public static int part2(List<String> data) {
        int oxygenRating = selectCandidate(data, SelectionStrategy.OXYGEN_RATING);
        int carbonDioxideRating = selectCandidate(data, SelectionStrategy.CARBON_DIOXIDE_RATING);

        return oxygenRating * carbonDioxideRating;
    }
}
