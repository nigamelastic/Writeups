filename="input.txt"

with open(filename) as file:
    input = [x.strip() for x in file.readlines()]


def part1(data):
    x = 0                             # X is current column
    total = 0                         # Count of trees
    map_width = len(data[0])
    map_height = len(data)
    for y in range(map_height):       # Iterate each row
        if data[y][x] == '#':         # Use x,y as coordinates to check for tree
            total += 1                # Count if tree
        x = (x + 3) % map_width       # Jump 3 steps right (modulus to keep within map)
    return total




def part2(data):
    def traverse(right, down):
      # Filter out jumped rows
      rows_hit = [
        row
        for idx, row
        in enumerate(data)
        if idx % down == 0
      ]

      # Filter out rows where we encounter a tree
      trees_encountered = [
        idx
        for idx, row
        in enumerate(rows_hit)
        if row[(idx * right) % len(row)] == '#'
      ]
      return len(trees_encountered)

    return traverse(1,1) * traverse(3,1) * traverse(5,1) * traverse(7,1) * traverse(1,2)

#print(part1(input))
print(part2(input))