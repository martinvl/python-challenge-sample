from sys import stdin

# loop through all the input lines
for line in stdin:
    i = map(int, line.split()) # parse all integers on current line

    print sum(i)
