$ git cat-file -p c45f26b
# Default is World
# Author: Day Fray (theMan@manmanguyman.com)

name = ARGV.first || "World"

puts "Hello, #{name}!"

