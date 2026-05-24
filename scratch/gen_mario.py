grid = [
    ".......RRRRR....",
    "......RRRRRRR...",
    "......BBBSKSSS..",
    ".....BSBSSSKSSS.",
    ".....BSBBSSSSSKS",
    ".....BBSSSSSSSS.",
    ".......SSSSSSS..",
    ".....RRR..RRRR..",
    "....RRRRLRRRRR..",
    "...RRRRLLLLRR...",
    "..WWRYLLLYRWW...",
    "..WWLLLLLLLWW...",
    "....LL...LL.....",
    "...BBB...BBB....",
    "..BBBB...BBBB..."
]
colors = {
    'R': '#e83000',
    'B': '#885000',
    'S': '#fca044',
    'L': '#0040f8',
    'W': '#ffffff',
    'Y': '#f8d820',
    'K': '#000000'
}
svg = '<g id="mario">\n'
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c in colors:
            svg += f'  <rect x="{x*3}" y="{y*3}" width="3" height="3" fill="{colors[c]}" />\n'
svg += '</g>'
with open('scratch/mario.txt', 'w') as f:
    f.write(svg)
