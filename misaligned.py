color_map = []

def capture_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)

def print_color_map(color_map):
    for entry in color_map:
        print(entry)

capture_color_map()
print_color_map(color_map)
assert(len(color_map) == 25), "Color map size should be 25"
assert(all('|' in entry for entry in color_map)), "Separator '|' missing in color map entries"
assert(all(entry.split('|')[0].strip().isdigit() for entry in color_map)), "Index should be a number"
assert(color_map[-1] == '24 | Violet | Slate')
assert(all(entry.find('|') - len(entry.split('|')[0]) == 2 for entry in color_map)), "Index alignment issue"
assert(all(entry.find('|', entry.find('|') + 1) - entry.find('|') - 1 == 6 for entry in color_map)), "Major color alignment issue"
assert(all(len(entry.split('|')[2]) == 6 for entry in color_map)), "Minor color alignment issue"
print("All is well (maybe!)\n")
