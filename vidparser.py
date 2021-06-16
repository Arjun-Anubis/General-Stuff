# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 12:52:33 2021

@author: anubi
"""
import cv2
from pytube import YouTube
import sys
framerate = 30
lskip = 40



l = sys.argv[1]
f = YouTube(l).streams.first().download()

    


if len(sys.argv) > 2:
    cam = cv2.VideoCapture(f)
    
    t = (int(sys.argv[2]) * 60 + int(sys.argv[3])) * framerate
    for i in range(t):
        cam.read()
    
    n = 1
    while True:
        
        ret, frame = cam.read()
        if ret:
            cv2.imwrite(f"qs/q{n}.jpg", frame)
            n+=1
            for i in range(framerate * lskip): cam.read()
        else:
            break