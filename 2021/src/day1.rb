inputs_path = File.join(File.dirname(__FILE__), '../inputs')
day1_input = File.readlines(File.join(inputs_path, 'day1.txt')).map(&:to_i)

def part1(depths)
  increased = 0

  depths[1..].zip(depths).each do |cur, prev|
    if cur > prev
      increased += 1
    end
  end

  increased
end

def part2(depths)
  increased = 0

  depths[3..].zip(depths).each do |cur, prev|
    if cur > prev
      increased += 1
    end
  end

  increased
end

test_input = [
  199,
  200,
  208,
  210,
  200,
  207,
  240,
  269,
  260,
  263
]

raise 'Test failed' unless part1(test_input) == 7
raise 'Test failed' unless part2(test_input) == 5

puts "Part 1 solution: #{part1(day1_input)}"
puts "Part 2 solution: #{part2(day1_input)}"
