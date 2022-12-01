elfs_carrying_calories = list()

with open("./input.txt") as file:    
    data = file.readline()
    elf_carrying = list()

    while data:
        if data == "\n":
            elfs_carrying_calories.append(sum(elf_carrying))
            elf_carrying.clear()
        else:
            data = int(data.rstrip())
            elf_carrying.append(data)
        data = file.readline()

# Part1
print(max(elfs_carrying_calories))

# Part2
elfs_sorted = sorted(elfs_carrying_calories)
print(sum(elfs_sorted[-3:]))