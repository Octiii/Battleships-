
grid_size = input("How big would you like the grid to be?")
"""selection = input("Please select a cell.")"""
alfabeth = "ABCDEFGJKLMNOPRSTUVWXYZ"
grid = []
def alfabeth_asinger():
    for z in alfabeth:
        letter = alfabeth[1:2]
    return letter

for x in range(int(grid_size)):
    x =  [
        alfabeth_asinger()
    ]
    
    for y in range(int(grid_size)):
        y = []
        x.append(y)
    grid.append(x)


"""
Print staments to check on code.
"""
for y in range(len(grid)):
    print(grid[y])
