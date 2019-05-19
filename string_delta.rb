# Finds differences between 2 strings

TEST_STRING_1 = "Hello!\nThis\nis\nTest String 1.\nDon't forget:\nYou succ"
TEST_STRING_2 = "Hello!\nThis\nis\nTest String 2.\nYeet"

def find_delta(str1, str2)
  lines1 = str1.split "\n"
  lines2 = str2.split "\n"

  lines1_unique = []
  lines2_unique = []

  # Finding lines that are in str1 but not in str2
  lines1.each do |line|
    lines1_unique.push line unless lines2.include? line   # Alternatively use regex instead fo include? no need for array then
  end

  # Finding lines that are in str2 but not in str1
  lines2.each do |line|
    lines2_unique.push line unless lines1.include? line
  end

  [lines1_unique, lines2_unique]
end


unique1, unique2 = find_delta(TEST_STRING_1, TEST_STRING_2)

puts "Unique 1:"
puts unique1

puts "---------------------------\nUnique 2:"
puts unique2
