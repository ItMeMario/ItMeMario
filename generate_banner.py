import re

# 5x7 Pixel Font Definitions (Uppercase, digits, and basic symbols)
FONT = {
    'A': ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    'B': ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    'C': ["01110", "10001", "10000", "10000", "10000", "10001", "01110"],
    'D': ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    'E': ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    'F': ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    'G': ["01110", "10001", "10000", "10111", "10001", "10001", "01110"],
    'H': ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    'I': ["01110", "00100", "00100", "00100", "00100", "00100", "01110"],
    'J': ["00111", "00010", "00010", "00010", "00010", "10010", "01100"],
    'K': ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    'L': ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    'M': ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    'N': ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    'O': ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    'P': ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    'Q': ["01110", "10001", "10001", "10001", "10101", "10011", "01101"],
    'R': ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    'S': ["01110", "10001", "01000", "00100", "00010", "10001", "01110"],
    'T': ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    'U': ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    'V': ["10001", "10001", "10001", "10001", "01010", "01010", "00100"],
    'W': ["10001", "10001", "10001", "10101", "10101", "11011", "10001"],
    'X': ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    'Y': ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    'Z': ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
    '0': ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    '1': ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    '2': ["01110", "10001", "00001", "00110", "01000", "10000", "11111"],
    '3': ["01110", "10001", "00001", "00110", "00001", "10001", "01110"],
    '4': ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    '5': ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
    '6': ["01110", "10000", "10000", "11110", "10001", "10001", "01110"],
    '7': ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    '8': ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    '9': ["01110", "10001", "10001", "01111", "00001", "10001", "01110"],
    ' ': ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
    '|': ["00100", "00100", "00100", "00100", "00100", "00100", "00100"],
    '-': ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
    '.': ["00000", "00000", "00000", "00000", "00000", "00000", "00100"],
    '>': ["10000", "01000", "00100", "00010", "00100", "01000", "10000"],
    '<': ["00001", "00010", "00100", "01000", "00100", "00010", "00001"],
}

def text_to_path(text, scale=1, letter_spacing=1):
    path_d = []
    x_offset = 0
    for char in text.upper():
        if char not in FONT:
            char = ' '
        grid = FONT[char]
        for r_idx, row in enumerate(grid):
            for c_idx, val in enumerate(row):
                if val == '1':
                    path_d.append(f"M {x_offset + c_idx * scale} {r_idx * scale} h {scale} v {scale} h -{scale} Z")
        x_offset += (5 + letter_spacing) * scale
    return "".join(path_d)

def get_text_width(text, scale=1, letter_spacing=1):
    return (len(text) * 5 + (len(text) - 1) * letter_spacing) * scale


def main():
    mario_char_block = """<!-- ========= MARIO CHARACTER (static position) ========= -->
  <g transform="translate(60, 100)">
    <g class="walk-f1">
      <rect x="16" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="20" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="24" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="28" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="32" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="16" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="20" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="24" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="28" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="32" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="36" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="40" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="44" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="8" width="4" height="4" fill="#6B3E08"/>
      <rect x="16" y="8" width="4" height="4" fill="#6B3E08"/>
      <rect x="20" y="8" width="4" height="4" fill="#6B3E08"/>
      <rect x="24" y="8" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="8" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="8" width="4" height="4" fill="#C8A000"/>
      <rect x="36" y="8" width="4" height="4" fill="#6B3E08"/>
      <rect x="8" y="12" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="16" y="12" width="4" height="4" fill="#6B3E08"/>
      <rect x="20" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="24" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="12" width="4" height="4" fill="#C8A000"/>
      <rect x="36" y="12" width="4" height="4" fill="#6B3E08"/>
      <rect x="40" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="8" y="16" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="16" y="16" width="4" height="4" fill="#6B3E08"/>
      <rect x="20" y="16" width="4" height="4" fill="#6B3E08"/>
      <rect x="24" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="36" y="16" width="4" height="4" fill="#C8A000"/>
      <rect x="40" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="44" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="8" y="20" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="20" width="4" height="4" fill="#6B3E08"/>
      <rect x="16" y="20" width="4" height="4" fill="#FBD000"/>
      <rect x="20" y="20" width="4" height="4" fill="#FBD000"/>
      <rect x="24" y="20" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="20" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="20" width="4" height="4" fill="#C8A000"/>
      <rect x="36" y="20" width="4" height="4" fill="#6B3E08"/>
      <rect x="16" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="20" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="24" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="36" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="8" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="16" y="28" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="24" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="28" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="32" y="28" width="4" height="4" fill="#003388"/>
      <rect x="0" y="32" width="4" height="4" fill="#FBD000"/>
      <rect x="4" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="8" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="16" y="32" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="32" width="4" height="4" fill="#0050CC"/>
      <rect x="24" y="32" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="32" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="36" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="40" y="32" width="4" height="4" fill="#003388"/>
      <rect x="44" y="32" width="4" height="4" fill="#FBD000"/>
      <rect x="0" y="36" width="4" height="4" fill="#FBD000"/>
      <rect x="4" y="36" width="4" height="4" fill="#FBD000"/>
      <rect x="8" y="36" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="36" width="4" height="4" fill="#0050CC"/>
      <rect x="16" y="36" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="36" width="4" height="4" fill="#FFD700"/>
      <rect x="24" y="36" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="36" width="4" height="4" fill="#0050CC"/>
      <rect x="32" y="36" width="4" height="4" fill="#E52521"/>
      <rect x="36" y="36" width="4" height="4" fill="#003388"/>
      <rect x="40" y="36" width="4" height="4" fill="#FBD000"/>
      <rect x="44" y="36" width="4" height="4" fill="#FBD000"/>
      <rect x="8" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="12" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="16" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="24" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="32" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="36" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="8" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="12" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="16" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="24" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="32" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="36" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="8" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="12" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="16" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="32" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="36" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="4" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="8" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="32" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="36" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="40" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="0" y="56" width="4" height="4" fill="#6B3E08"/>
      <rect x="4" y="56" width="4" height="4" fill="#6B3E08"/>
      <rect x="8" y="56" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="56" width="4" height="4" fill="#6B3E08"/>
      <rect x="32" y="56" width="4" height="4" fill="#6B3E08"/>
      <rect x="36" y="56" width="4" height="4" fill="#6B3E08"/>
      <rect x="40" y="56" width="4" height="4" fill="#6B3E08"/>
      <rect x="44" y="56" width="4" height="4" fill="#6B3E08"/>
    </g>
    <g class="walk-f2">
      <rect x="16" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="20" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="24" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="28" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="32" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="16" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="20" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="24" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="28" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="32" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="36" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="40" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="44" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="8" width="4" height="4" fill="#6B3E08"/>
      <rect x="16" y="8" width="4" height="4" fill="#6B3E08"/>
      <rect x="20" y="8" width="4" height="4" fill="#6B3E08"/>
      <rect x="24" y="8" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="8" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="8" width="4" height="4" fill="#C8A000"/>
      <rect x="36" y="8" width="4" height="4" fill="#6B3E08"/>
      <rect x="8" y="12" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="16" y="12" width="4" height="4" fill="#6B3E08"/>
      <rect x="20" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="24" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="12" width="4" height="4" fill="#C8A000"/>
      <rect x="36" y="12" width="4" height="4" fill="#6B3E08"/>
      <rect x="40" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="8" y="16" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="16" y="16" width="4" height="4" fill="#6B3E08"/>
      <rect x="20" y="16" width="4" height="4" fill="#6B3E08"/>
      <rect x="24" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="36" y="16" width="4" height="4" fill="#C8A000"/>
      <rect x="40" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="44" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="8" y="20" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="20" width="4" height="4" fill="#6B3E08"/>
      <rect x="16" y="20" width="4" height="4" fill="#FBD000"/>
      <rect x="20" y="20" width="4" height="4" fill="#FBD000"/>
      <rect x="24" y="20" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="20" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="20" width="4" height="4" fill="#C8A000"/>
      <rect x="36" y="20" width="4" height="4" fill="#6B3E08"/>
      <rect x="16" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="20" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="24" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="36" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="12" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="16" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="20" y="28" width="4" height="4" fill="#0050CC"/>
      <rect x="24" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="28" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="8" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="16" y="32" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="32" width="4" height="4" fill="#0050CC"/>
      <rect x="24" y="32" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="32" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="36" y="32" width="4" height="4" fill="#003388"/>
      <rect x="4" y="36" width="4" height="4" fill="#E52521"/>
      <rect x="8" y="36" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="36" width="4" height="4" fill="#0050CC"/>
      <rect x="16" y="36" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="36" width="4" height="4" fill="#FFD700"/>
      <rect x="24" y="36" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="36" width="4" height="4" fill="#0050CC"/>
      <rect x="32" y="36" width="4" height="4" fill="#E52521"/>
      <rect x="36" y="36" width="4" height="4" fill="#E52521"/>
      <rect x="40" y="36" width="4" height="4" fill="#003388"/>
      <rect x="4" y="40" width="4" height="4" fill="#FBD000"/>
      <rect x="8" y="40" width="4" height="4" fill="#FBD000"/>
      <rect x="12" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="16" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="24" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="32" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="36" y="40" width="4" height="4" fill="#FBD000"/>
      <rect x="40" y="40" width="4" height="4" fill="#FBD000"/>
      <rect x="12" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="16" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="24" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="32" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="8" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="12" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="32" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="36" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="4" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="8" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="32" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="36" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="40" y="52" width="4" height="4" fill="#6B3E08"/>
    </g>
    <g class="walk-f3">
      <rect x="16" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="20" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="24" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="28" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="32" y="0" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="16" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="20" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="24" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="28" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="32" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="36" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="40" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="44" y="4" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="8" width="4" height="4" fill="#6B3E08"/>
      <rect x="16" y="8" width="4" height="4" fill="#6B3E08"/>
      <rect x="20" y="8" width="4" height="4" fill="#6B3E08"/>
      <rect x="24" y="8" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="8" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="8" width="4" height="4" fill="#C8A000"/>
      <rect x="36" y="8" width="4" height="4" fill="#6B3E08"/>
      <rect x="8" y="12" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="16" y="12" width="4" height="4" fill="#6B3E08"/>
      <rect x="20" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="24" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="12" width="4" height="4" fill="#C8A000"/>
      <rect x="36" y="12" width="4" height="4" fill="#6B3E08"/>
      <rect x="40" y="12" width="4" height="4" fill="#FBD000"/>
      <rect x="8" y="16" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="16" y="16" width="4" height="4" fill="#6B3E08"/>
      <rect x="20" y="16" width="4" height="4" fill="#6B3E08"/>
      <rect x="24" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="36" y="16" width="4" height="4" fill="#C8A000"/>
      <rect x="40" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="44" y="16" width="4" height="4" fill="#FBD000"/>
      <rect x="8" y="20" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="20" width="4" height="4" fill="#6B3E08"/>
      <rect x="16" y="20" width="4" height="4" fill="#FBD000"/>
      <rect x="20" y="20" width="4" height="4" fill="#FBD000"/>
      <rect x="24" y="20" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="20" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="20" width="4" height="4" fill="#C8A000"/>
      <rect x="36" y="20" width="4" height="4" fill="#6B3E08"/>
      <rect x="16" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="20" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="24" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="28" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="32" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="36" y="24" width="4" height="4" fill="#FBD000"/>
      <rect x="12" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="16" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="20" y="28" width="4" height="4" fill="#0050CC"/>
      <rect x="24" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="28" y="28" width="4" height="4" fill="#E52521"/>
      <rect x="32" y="28" width="4" height="4" fill="#003388"/>
      <rect x="12" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="16" y="32" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="32" width="4" height="4" fill="#0050CC"/>
      <rect x="24" y="32" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="32" y="32" width="4" height="4" fill="#E52521"/>
      <rect x="36" y="32" width="4" height="4" fill="#003388"/>
      <rect x="8" y="36" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="36" width="4" height="4" fill="#0050CC"/>
      <rect x="16" y="36" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="36" width="4" height="4" fill="#FFD700"/>
      <rect x="24" y="36" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="36" width="4" height="4" fill="#0050CC"/>
      <rect x="32" y="36" width="4" height="4" fill="#E52521"/>
      <rect x="36" y="36" width="4" height="4" fill="#E52521"/>
      <rect x="40" y="36" width="4" height="4" fill="#003388"/>
      <rect x="8" y="40" width="4" height="4" fill="#E52521"/>
      <rect x="12" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="16" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="24" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="32" y="40" width="4" height="4" fill="#0050CC"/>
      <rect x="36" y="40" width="4" height="4" fill="#FBD000"/>
      <rect x="40" y="40" width="4" height="4" fill="#FBD000"/>
      <rect x="12" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="16" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="20" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="24" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="32" y="44" width="4" height="4" fill="#0050CC"/>
      <rect x="12" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="16" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="28" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="32" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="36" y="48" width="4" height="4" fill="#0050CC"/>
      <rect x="8" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="16" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="28" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="32" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="36" y="52" width="4" height="4" fill="#6B3E08"/>
      <rect x="4" y="56" width="4" height="4" fill="#6B3E08"/>
      <rect x="8" y="56" width="4" height="4" fill="#6B3E08"/>
      <rect x="12" y="56" width="4" height="4" fill="#6B3E08"/>
      <rect x="28" y="56" width="4" height="4" fill="#6B3E08"/>
      <rect x="32" y="56" width="4" height="4" fill="#6B3E08"/>
      <rect x="36" y="56" width="4" height="4" fill="#6B3E08"/>
    </g>
  </g>"""

    # Generate custom font paths
    title_text = "ItMeMario"
    subtitle_text = "FULL-STACK | OPEN SOURCE | GAMING"
    start_text = "> PRESS START <"
    score_lbl = "SCORE"
    score_val = "001337"
    world_lbl = "WORLD"
    world_val = "1-1"

    # Scale settings
    title_scale = 5
    sub_scale = 2
    hud_scale = 1.5
    start_scale = 1.5
    spacing = 1

    title_w = get_text_width(title_text, title_scale, spacing)
    sub_w = get_text_width(subtitle_text, sub_scale, spacing)
    start_w = get_text_width(start_text, start_scale, spacing)

    title_path = text_to_path(title_text, title_scale, spacing)
    sub_path = text_to_path(subtitle_text, sub_scale, spacing)
    start_path = text_to_path(start_text, start_scale, spacing)

    # HUD paths
    score_lbl_path = text_to_path(score_lbl, hud_scale, spacing)
    score_val_path = text_to_path(score_val, hud_scale, spacing)
    world_lbl_path = text_to_path(world_lbl, hud_scale, spacing)
    world_val_path = text_to_path(world_val, hud_scale, spacing)

    svg_content = f"""<svg width="800" height="200" viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">
  <defs>
    <style>
      /* ---- Parallax Scrolling ---- */
      @keyframes scrollFar  {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-800px); }} }}
      @keyframes scrollMid  {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-800px); }} }}
      @keyframes scrollNear {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-800px); }} }}

      /* ---- Character Walk ---- */
      @keyframes walkCycle {{
        0%, 33.32%   {{ opacity: 1; }}
        33.34%, 100% {{ opacity: 0; }}
      }}

      /* ---- Floating Title ---- */
      @keyframes float {{
        0%, 100% {{ transform: translateY(0px); }}
        50%      {{ transform: translateY(-6px); }}
      }}

      /* ---- Bounce (Question Block) ---- */
      @keyframes bounce {{
        0%, 100% {{ transform: translateY(0px); }}
        50%      {{ transform: translateY(-4px); }}
      }}

      /* ---- Coin Spin ---- */
      @keyframes coinSpin {{
        0%   {{ transform: scaleX(1); }}
        25%  {{ transform: scaleX(0.3); }}
        50%  {{ transform: scaleX(0); }}
        75%  {{ transform: scaleX(0.3); }}
        100% {{ transform: scaleX(1); }}
      }}

      /* ---- Retro Rainbow Text ---- */
      @keyframes rainbow {{
        0%   {{ fill: #FF3333; }}
        20%  {{ fill: #FF8800; }}
        40%  {{ fill: #FFFF00; }}
        60%  {{ fill: #00FF00; }}
        80%  {{ fill: #0088FF; }}
        100% {{ fill: #FF3333; }}
      }}

      /* ---- Sparkle / Twinkle ---- */
      @keyframes sparkle {{
        0%, 100% {{ opacity: 0.3; transform: scale(0.8); }}
        50%      {{ opacity: 1;   transform: scale(1.2); }}
      }}

      /* ---- Blink Cursor ---- */
      @keyframes blink {{
        0%, 49%  {{ opacity: 1; }}
        50%, 100% {{ opacity: 0; }}
      }}

      /* ---- Glow Pulse ---- */
      @keyframes glowPulse {{
        0%, 100% {{ filter: drop-shadow(0 0 2px rgba(255,215,0,0.5)); }}
        50%      {{ filter: drop-shadow(0 0 8px rgba(255,215,0,0.9)); }}
      }}

      /* ---- Classes ---- */
      .layer-far  {{ animation: scrollFar  30s linear infinite; }}
      .layer-mid  {{ animation: scrollMid  18s linear infinite; }}
      .layer-near {{ animation: scrollNear  8s linear infinite; }}

      .walk-f1, .walk-f2, .walk-f3 {{
        opacity: 0;
        animation: walkCycle 0.45s steps(1) infinite;
      }}
      .walk-f1 {{ animation-delay: 0.000s; }}
      .walk-f2 {{ animation-delay: 0.150s; }}
      .walk-f3 {{ animation-delay: 0.300s; }}

      .float   {{ animation: float 3s ease-in-out infinite; }}
      .bounce  {{ animation: bounce 1.5s ease-in-out infinite; }}
      .coin    {{ animation: coinSpin 1.2s linear infinite; transform-origin: center; }}
      .rainbow {{ animation: rainbow 6s linear infinite; }}
      .sparkle {{ animation: sparkle 2s ease-in-out infinite; }}
      .blink-cursor {{ animation: blink 1s step-end infinite; }}
      .glow    {{ animation: glowPulse 2s ease-in-out infinite; }}

      /* ---- Responsive Light/Dark Mode Sky and Cloud styling ---- */
      .sky-bg {{
        fill: url(#sky-dark);
      }}
      .cloud-element {{
        fill: #ffffff;
        opacity: 0.12;
      }}
      .star-element {{
        display: block;
      }}
      .hud-text {{
        fill: #FFFFFF;
        opacity: 0.75;
      }}

      @media (prefers-color-scheme: light) {{
        .sky-bg {{
          fill: url(#sky-light);
        }}
        .cloud-element {{
          fill: #ffffff;
          opacity: 0.75;
        }}
        .star-element {{
          display: none;
        }}
        .hud-text {{
          fill: #000000;
          opacity: 0.65;
        }}
      }}
    </style>

    <!-- Dark Mode Sky Gradient -->
    <linearGradient id="sky-dark" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#0a051d"/>
      <stop offset="60%"  stop-color="#190e38"/>
      <stop offset="100%" stop-color="#341b54"/>
    </linearGradient>

    <!-- Light Mode Sky Gradient -->
    <linearGradient id="sky-light" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#5c94fc"/>
      <stop offset="70%"  stop-color="#80b0ff"/>
      <stop offset="100%" stop-color="#a0c8ff"/>
    </linearGradient>

    <!-- Ground Brick Pattern -->
    <pattern id="brick" width="32" height="16" patternUnits="userSpaceOnUse">
      <rect width="32" height="16" fill="#C84C0C"/>
      <rect x="0"  y="0"  width="15" height="7" fill="#E87040" rx="1"/>
      <rect x="17" y="0"  width="15" height="7" fill="#E87040" rx="1"/>
      <rect x="8"  y="9"  width="15" height="7" fill="#E87040" rx="1"/>
      <rect x="25" y="9"  width="7"  height="7" fill="#E87040" rx="1"/>
      <rect x="0"  y="9"  width="6"  height="7" fill="#E87040" rx="1"/>
    </pattern>

    <!-- Twinkle Star Shape -->
    <g id="star">
      <polygon points="0,-4 1,-1 4,-1 1.5,1 2.5,4 0,2 -2.5,4 -1.5,1 -4,-1 -1,-1" fill="#FFD700"/>
    </g>

    <!-- Cloud Graphic -->
    <g id="cloud">
      <ellipse cx="30" cy="18" rx="26" ry="10" class="cloud-element"/>
      <ellipse cx="48" cy="13" rx="18" ry="8" class="cloud-element"/>
      <ellipse cx="14" cy="14" rx="14" ry="8" class="cloud-element"/>
    </g>

    <!-- Coin Graphics -->
    <g id="coin-def">
      <ellipse cx="8" cy="10" rx="5" ry="8" fill="#FFD700" stroke="#CC9900" stroke-width="1.5"/>
      <ellipse cx="8" cy="10" rx="2" ry="6" fill="#FFEE66" opacity="0.6"/>
    </g>
  </defs>

  <!-- ========= BACKGROUND ========= -->
  <rect width="100%" height="100%" class="sky-bg"/>

  <!-- Far Layer: Twinkling Stars (Dark Mode Only) -->
  <g class="layer-far star-element">
    <use href="#star" x="60"   y="20"  class="sparkle" style="animation-delay: 0s;"/>
    <use href="#star" x="150"  y="45"  class="sparkle" style="animation-delay: 0.7s;"/>
    <use href="#star" x="280"  y="15"  class="sparkle" style="animation-delay: 1.2s;"/>
    <use href="#star" x="400"  y="35"  class="sparkle" style="animation-delay: 0.3s;"/>
    <use href="#star" x="520"  y="10"  class="sparkle" style="animation-delay: 1.8s;"/>
    <use href="#star" x="650"  y="40"  class="sparkle" style="animation-delay: 0.5s;"/>
    <use href="#star" x="750"  y="25"  class="sparkle" style="animation-delay: 1.0s;"/>
    <!-- Duplicate for loop -->
    <use href="#star" x="860"  y="20"  class="sparkle" style="animation-delay: 0s;"/>
    <use href="#star" x="950"  y="45"  class="sparkle" style="animation-delay: 0.7s;"/>
    <use href="#star" x="1080" y="15"  class="sparkle" style="animation-delay: 1.2s;"/>
    <use href="#star" x="1200" y="35"  class="sparkle" style="animation-delay: 0.3s;"/>
    <use href="#star" x="1320" y="10"  class="sparkle" style="animation-delay: 1.8s;"/>
    <use href="#star" x="1450" y="40"  class="sparkle" style="animation-delay: 0.5s;"/>
    <use href="#star" x="1550" y="25"  class="sparkle" style="animation-delay: 1.0s;"/>
  </g>

  <!-- Mid Layer: Parallax Clouds -->
  <g class="layer-mid">
    <use href="#cloud" x="80"  y="25"/>
    <use href="#cloud" x="300" y="50"/>
    <use href="#cloud" x="560" y="15"/>
    <use href="#cloud" x="720" y="45"/>
    <!-- Duplicate -->
    <use href="#cloud" x="880"  y="25"/>
    <use href="#cloud" x="1100" y="50"/>
    <use href="#cloud" x="1360" y="15"/>
    <use href="#cloud" x="1520" y="45"/>
  </g>

  <!-- Near Layer: Ground, pipes, blocks, coins -->
  <g class="layer-near">
    <!-- Ground -->
    <rect y="168" width="1600" height="32" fill="url(#brick)"/>
    <rect y="166" width="1600" height="3" fill="#88CC44"/>

    <!-- Question Blocks -->
    <g class="bounce" style="animation-delay: 0s;">
      <g transform="translate(200,96)">
        <rect width="32" height="32" fill="#E07020" stroke="#6B3E08" stroke-width="2" rx="1"/>
        <rect x="2" y="2" width="28" height="28" fill="#FBD000" rx="1"/>
        <rect x="4" y="4" width="24" height="24" fill="#E07020" rx="1"/>
        <!-- Custom Drawn pixel art '?' symbol inside block -->
        <path d="M 12 8 h 8 v 4 h -4 v 4 h -4 v -4 h 4 v -2 h -4 Z M 12 18 h 4 v 4 h -4 Z" fill="#FBD000"/>
      </g>
    </g>
    <g class="bounce" style="animation-delay: 0.3s;">
      <g transform="translate(236,96)">
        <rect width="32" height="32" fill="#E07020" stroke="#6B3E08" stroke-width="2" rx="1"/>
        <rect x="2" y="2" width="28" height="28" fill="#FBD000" rx="1"/>
        <rect x="4" y="4" width="24" height="24" fill="#E07020" rx="1"/>
        <path d="M 12 8 h 8 v 4 h -4 v 4 h -4 v -4 h 4 v -2 h -4 Z M 12 18 h 4 v 4 h -4 Z" fill="#FBD000"/>
      </g>
    </g>
    <g class="bounce" style="animation-delay: 0.6s;">
      <g transform="translate(272,96)">
        <rect width="32" height="32" fill="#E07020" stroke="#6B3E08" stroke-width="2" rx="1"/>
        <rect x="2" y="2" width="28" height="28" fill="#FBD000" rx="1"/>
        <rect x="4" y="4" width="24" height="24" fill="#E07020" rx="1"/>
        <path d="M 12 8 h 8 v 4 h -4 v 4 h -4 v -4 h 4 v -2 h -4 Z M 12 18 h 4 v 4 h -4 Z" fill="#FBD000"/>
      </g>
    </g>

    <!-- Green Pipes -->
    <g transform="translate(500,118)">
      <rect x="0" y="0" width="44" height="14" fill="#00AA00" stroke="#004400" stroke-width="1.5" rx="1"/>
      <rect x="3" y="3" width="8" height="8" fill="#55DD55"/>
      <rect x="5" y="14" width="34" height="36" fill="#00AA00" stroke="#004400" stroke-width="1.5"/>
      <rect x="8" y="14" width="6" height="36" fill="#55DD55"/>
    </g>
    <g transform="translate(640,102)">
      <rect x="0" y="0" width="44" height="14" fill="#00AA00" stroke="#004400" stroke-width="1.5" rx="1"/>
      <rect x="3" y="3" width="8" height="8" fill="#55DD55"/>
      <rect x="5" y="14" width="34" height="52" fill="#00AA00" stroke="#004400" stroke-width="1.5"/>
      <rect x="8" y="14" width="6" height="52" fill="#55DD55"/>
    </g>

    <!-- Coins (Floating above blocks) -->
    <g class="coin glow" style="animation-delay:0s;"   transform="translate(208, 72)"><use href="#coin-def"/></g>
    <g class="coin glow" style="animation-delay:0.3s;" transform="translate(244, 72)"><use href="#coin-def"/></g>
    <g class="coin glow" style="animation-delay:0.6s;" transform="translate(280, 72)"><use href="#coin-def"/></g>

    <!-- Ground Level Coins -->
    <g class="coin glow" style="animation-delay:0.1s;" transform="translate(710, 125)"><use href="#coin-def"/></g>
    <g class="coin glow" style="animation-delay:0.4s;" transform="translate(730, 125)"><use href="#coin-def"/></g>
    <g class="coin glow" style="animation-delay:0.7s;" transform="translate(750, 125)"><use href="#coin-def"/></g>

    <!-- ==== DUPLICATES FOR SEAMLESS LOOPING ==== -->
    <g class="bounce" style="animation-delay: 0s;">
      <g transform="translate(1000,96)">
        <rect width="32" height="32" fill="#E07020" stroke="#6B3E08" stroke-width="2" rx="1"/>
        <rect x="2" y="2" width="28" height="28" fill="#FBD000" rx="1"/>
        <rect x="4" y="4" width="24" height="24" fill="#E07020" rx="1"/>
        <path d="M 12 8 h 8 v 4 h -4 v 4 h -4 v -4 h 4 v -2 h -4 Z M 12 18 h 4 v 4 h -4 Z" fill="#FBD000"/>
      </g>
    </g>
    <g class="bounce" style="animation-delay: 0.3s;">
      <g transform="translate(1036,96)">
        <rect width="32" height="32" fill="#E07020" stroke="#6B3E08" stroke-width="2" rx="1"/>
        <rect x="2" y="2" width="28" height="28" fill="#FBD000" rx="1"/>
        <rect x="4" y="4" width="24" height="24" fill="#E07020" rx="1"/>
        <path d="M 12 8 h 8 v 4 h -4 v 4 h -4 v -4 h 4 v -2 h -4 Z M 12 18 h 4 v 4 h -4 Z" fill="#FBD000"/>
      </g>
    </g>
    <g class="bounce" style="animation-delay: 0.6s;">
      <g transform="translate(1072,96)">
        <rect width="32" height="32" fill="#E07020" stroke="#6B3E08" stroke-width="2" rx="1"/>
        <rect x="2" y="2" width="28" height="28" fill="#FBD000" rx="1"/>
        <rect x="4" y="4" width="24" height="24" fill="#E07020" rx="1"/>
        <path d="M 12 8 h 8 v 4 h -4 v 4 h -4 v -4 h 4 v -2 h -4 Z M 12 18 h 4 v 4 h -4 Z" fill="#FBD000"/>
      </g>
    </g>
    <g transform="translate(1300,118)">
      <rect x="0" y="0" width="44" height="14" fill="#00AA00" stroke="#004400" stroke-width="1.5" rx="1"/>
      <rect x="3" y="3" width="8" height="8" fill="#55DD55"/>
      <rect x="5" y="14" width="34" height="36" fill="#00AA00" stroke="#004400" stroke-width="1.5"/>
      <rect x="8" y="14" width="6" height="36" fill="#55DD55"/>
    </g>
    <g transform="translate(1440,102)">
      <rect x="0" y="0" width="44" height="14" fill="#00AA00" stroke="#004400" stroke-width="1.5" rx="1"/>
      <rect x="3" y="3" width="8" height="8" fill="#55DD55"/>
      <rect x="5" y="14" width="34" height="52" fill="#00AA00" stroke="#004400" stroke-width="1.5"/>
      <rect x="8" y="14" width="6" height="52" fill="#55DD55"/>
    </g>
    <g class="coin glow" style="animation-delay:0s;"   transform="translate(1008, 72)"><use href="#coin-def"/></g>
    <g class="coin glow" style="animation-delay:0.3s;" transform="translate(1044, 72)"><use href="#coin-def"/></g>
    <g class="coin glow" style="animation-delay:0.6s;" transform="translate(1080, 72)"><use href="#coin-def"/></g>
    <g class="coin glow" style="animation-delay:0.1s;" transform="translate(1510, 125)"><use href="#coin-def"/></g>
    <g class="coin glow" style="animation-delay:0.4s;" transform="translate(1530, 125)"><use href="#coin-def"/></g>
    <g class="coin glow" style="animation-delay:0.7s;" transform="translate(1550, 125)"><use href="#coin-def"/></g>
  </g>

  <!-- ========= MARIO CHARACTER ========= -->
  {mario_char_block}

  <!-- ========= TEXT OVERLAY (Pixel Art Paths) ========= -->
  <!-- 1. Main Title: "ItMeMario" -->
  <g class="float" transform="translate(400, 32)">
    <!-- 3D Shadow -->
    <path d="{title_path}" fill="#000000" opacity="0.5" transform="translate(2, 2) translate(-{title_w/2}, 0)"/>
    <!-- Animated Rainbow Title -->
    <path d="{title_path}" class="rainbow" transform="translate(-{title_w/2}, 0)"/>
  </g>

  <!-- 2. Subtitle: "FULL-STACK | OPEN SOURCE | GAMING" -->
  <g transform="translate(400, 74)">
    <path d="{sub_path}" fill="#000000" opacity="0.4" transform="translate(1, 1) translate(-{sub_w/2}, 0)"/>
    <path d="{sub_path}" fill="#FFEEAA" transform="translate(-{sub_w/2}, 0)"/>
  </g>

  <!-- 3. Blinking "PRESS START" -->
  <g class="blink-cursor" transform="translate(400, 146)">
    <path d="{start_path}" fill="#FFD700" transform="translate(-{start_w/2}, 0)"/>
  </g>

  <!-- ========= HUD HEADS UP DISPLAY ========= -->
  <!-- Score Display (Top Left) -->
  <g transform="translate(16, 12)">
    <path d="{score_lbl_path}" class="hud-text"/>
    <path d="{score_val_path}" class="hud-text" transform="translate(0, 13)"/>
  </g>

  <!-- World Display (Top Right) -->
  <g transform="translate(734, 12)">
    <path d="{world_lbl_path}" class="hud-text"/>
    <path d="{world_val_path}" class="hud-text" transform="translate(14, 13)"/>
  </g>
</svg>
"""

    with open('banner.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Success: banner.svg created successfully with custom pixel-art fonts.")

if __name__ == '__main__':
    main()
