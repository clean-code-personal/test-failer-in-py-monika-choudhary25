color_map = []

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


capture_color_map()

assert(len(color_map) == 25), "Color map size should be 25"
assert(all('|' in entry for entry in color_map)), "Separator '|' missing in color map entries"
assert(all(entry.split('|')[0].strip().isdigit() for entry in color_map)), "Index should be a number"
print("All is well (maybe!)\n")
