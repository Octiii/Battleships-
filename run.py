
grid_size = input("How big would you like the grid to be?")
"""selection = input("Please select a cell.")"""
grid = []

for x in range(int(grid_size)):
    x = []
    
    for y in range(int(grid_size)):
        y = []
        x.append(y)
    grid.append(x)


"""
Print staments to check on code.
"""
for y in range(len(grid)):
    print(grid[y])
