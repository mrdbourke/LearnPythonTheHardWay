TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for item in TILES:
    if item == '||':
        print() #print() prints out on a new line by default
    else:
        print(item, end="")
