def tree_count(rise, run, rows):
    row = 0
    col = 0
    count = 0
    while(row < len(rows)):
        if rows[row][col] == '#':
            count = count + 1
        col = (col + run) % len(rows[row])
        row = row + rise
    return count

with open("input.txt") as input:
    rows = input.read().splitlines()
    x = tree_count(1, 1, rows)
    y = tree_count(1, 3, rows)
    z = tree_count(1, 5, rows)
    w = tree_count(1, 7, rows)
    v = tree_count(2, 1, rows)
    print(x, y, z, w, v, x * y * z * w * v)
