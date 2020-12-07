with open("input.txt") as input:
    rows = input.read().splitlines()
    col = 0
    tree_count = 0
    for row in rows:
        if row[col] == '#':
            tree_count = tree_count + 1
        col = (col + 3) % len(row)
    print(tree_count)
