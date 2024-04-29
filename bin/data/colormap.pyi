def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    h = int(hex_str, 16)
    r = h // 0x10000
    h %= 0x10000
    g = h // 0x100
    b = h % 0x100
    return (r, g, b)

def get_colors():
    start_hex = "#02b1eb"
    end_hex = "#000000"
    curr_rgb = hex_to_rgb(start_hex)
    while curr_rgb != hex_to_rgb(end_hex):
        yield curr_rgb
        curr_rgb = increment_rgb(curr_rgb)

def increment_rgb(rgb):
    r, g, b = rgb
    if r < 255:
        r += 1
    elif g < 255:
        g += 1
        r = 0
    else:
        b += 1
        g = r = 0
    return r, g, b

with open('color_map.txt', 'w') as f:
    for i, rgb in enumerate(get_colors()):
        if i > 0 and i % 48 == 0:
            print('\n', end='', flush=True)
        print(f'0x{rgb[0]:02x}, 0x{rgb[1]:02x}, 0x{rgb[2]:02x}', end=' ', file=f)
print()
