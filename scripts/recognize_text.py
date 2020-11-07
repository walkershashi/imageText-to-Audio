#import required python modules
import cv2 # opencv
import pytesseract # tesseract
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import glob
import os

def recognize_text(image):
    org_img = image
    # Image Resize
    resize_img = cv2.resize(
        org_img, None, fx = 2, fy = 2, 
        interpolation = cv2.INTER_CUBIC
    )

    # Converting to Gray Scale
    filtered_grayscale_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)

    # Using Gaussian Blur
    gaussian_blur_img = cv2.GaussianBlur(filtered_grayscale_img, (5, 5), 0)
    
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    text_img = pytesseract.image_to_string(
        gaussian_blur_img
    )

    text_img = text_img.replace("\n", " ")
    return text_img
