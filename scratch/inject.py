import io

with io.open('scratch/mario.txt', 'r', encoding='utf-8') as f:
    mario_svg = f.read()

with io.open('github-banner.svg', 'r', encoding='utf-8') as f:
    banner = f.read()

banner = banner.replace('</defs>', mario_svg + '\n  </defs>', 1)
banner = banner.replace('<!-- 6. TEXTOS -->', '<!-- Personagem Mario -->\n  <g id="mario-container" transform="translate(250, 160)">\n    <use href="#mario" x="0" y="0" />\n  </g>\n\n  <!-- 6. TEXTOS -->')

with io.open('github-banner.svg', 'w', encoding='utf-8') as f:
    f.write(banner)
