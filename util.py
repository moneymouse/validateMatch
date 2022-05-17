import cv2
import numpy as np

# img = cv2.imread('imgs/background6.jpg',0)

pattern = cv2.imread('imgs/pattern.jpg',0)

pattern_second = cv2.imread('imgs/patternD.jpg',0)


def get_pattern():
    ret,pattern_t = cv2.threshold(pattern,10,255,cv2.THRESH_BINARY)
    return pattern_t

def get_bg_threshold(src):
    img = cv2.imread(src,0)
    ret,dst = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    return dst

# dst = get_bg_threshold(img)

def safe_sum(d,pat):
    sum = d ^ pat
    sum = sum.sum()
    return sum

def safe_sum_s(d,pat):
    ret, pattern_s = cv2.threshold(pattern_second,10,255,cv2.THRESH_BINARY)
    sum = d ^ pat
    sum = sum ^ pattern_s
    sum = sum.sum(where = (255-pattern_s).astype(np.bool8))
    return sum


