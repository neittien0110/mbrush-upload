#!/usr/bin/env python3

from sre_constants import JUMP
from turtle import goto
import mbrush
import numpy as np
from PIL import Image
import getopt
import winsound
import sys

filename = None
'''Tên file ảnh cần in'''
mBrushIP = "192.168.88.1"
'''Địa chỉ IP máy in mBrush. Mặc định là 192.168.88.1, hoặc có thể là 192.168.44.1'''
zoom = 1
''' Tỉ lệ zoom ảnh để vừa khít với độ cao tối đa 1.44 cm. Giá trị phải 0.2<= .. <=1. Mặc định = 1.'''

def param_parser():
    global filename
    global mBrushIP
    global zoom
    """ Phân tích tham số dòng lệnh """
    argv = sys.argv[1:]
    if len(argv) < 2:
        print("upload.py -f <image> -i <mBrush IP> [-z 0.8]")
        exit(-2)
            
    try:
        opts, args = getopt.getopt(argv, "f:i:z:", ["file=","ip=","zoom="])
    except:
        print("upload.py -f <image> [-i <mBrushIP=192.168.88.1>] [-z 0.8]")
        exit(-1)
  
    for opt, arg in opts:
        if opt in ['-f', "--file"]:
            filename = arg
        elif opt in ['-i', "--ip"]:
            mBrushIP = arg
        elif opt in ['-z', "--zoom"]:
            zoom = float(arg)

#Phân tích tham số dòng lệnh
param_parser()
print( "Image: " + filename);   
print( "mBrush: http://{0}/".format(mBrushIP));


ImageData = Image.open(filename)

img = np.array(ImageData)
mbrush.print_rgb(img, mBrushIP, zoom)

# Phát tiếng kêu và kết thúc luôn
winsound.Beep(440, 250)
exit(0)

