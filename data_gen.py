"""
Works only on Windows OS
The function is designed to prepare the files necessary to demonstrate the operation of the service.

Returns:
    CSV file - conf.csv
    Folder "static" with demo images
"""

import os
import random
from PIL import Image, ImageDraw, ImageFont

folder = 'static'
if os.path.exists(folder):
    pass
else:
    os.mkdir(f'{folder}')

N_PICTURES = 30

N_SHOW_MAX = 5
N_SHOW_MIN = 15

font = ImageFont.truetype('arial.ttf', size=150)

NUMBERS_COORDINATES = {1: (55, 2.5), 2: (205, 2.5), 3: (355, 2.5), 4: (55, 162.5), 5: (205, 162.5), 6: (355, 162.5),
                       7: (55, 322.5), 8: (205, 322.5), 9: (355, 322.5), 0: (205, 482.5)}

file = open('conf.csv', 'w')
for count in range(N_PICTURES):
    string = f'f{count};' + str(random.randint(N_SHOW_MAX, N_SHOW_MIN))
    img = Image.new('RGBA', (500, 650), 'black')
    idraw = ImageDraw.Draw(img)
    for num in range(10):
        if random.choice([True, False]):
            idraw.text(NUMBERS_COORDINATES[num], str(num), font=font)
            string += f';n{num}'

    file.write(string + '\n')
    img.save(f'static/f{count}.png')

file.close()
