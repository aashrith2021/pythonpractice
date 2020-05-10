# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 23:42:02 2020

@author: Koti
"""

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("charac/plates/plate1.jpg" )
cv2.imshow("Image",img)