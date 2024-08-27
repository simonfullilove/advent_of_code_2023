def solve_nonogram_row(clues, row_size):
    row = [0] * row_size  # Initialize an empty row

    # Helper function to check if a group of cells can be placed at a given position
    def can_place(clue, position):
        return all(row[position + j] == 0 for j in range(clue))

    # Place filled cells based on the clues
    position = 0
    for clue in clues:
        while position < row_size and not can_place(clue, position):
            position += 1

        if position == row_size:
            break  # Unable to place the current clue

        row[position : position + clue] = [1] * clue
        position += clue + 1  # Move to the next possible position

    return row


# Create grid from input
f = open("input2.txt")
# grid = [list(line.rstrip()) for line in f]

for line in f.readlines():
    springs, pattern = line.split()
    pattern = [int(x) for x in pattern.split(",")]
    print(springs)
    print(pattern)

    # Example usage with clues [2, 1, 3] and row size 10
    clues = pattern
    row_size = len(springs)
    result = solve_nonogram_row(clues, row_size)
    print(result)










