from match import match
from util import get_bg_threshold, get_pattern
import cv2

def main():
    dst = get_bg_threshold("imgs/background3.jpg")
    pattern = get_pattern()
    pattern_row, pattern_col = pattern.shape
    y,x = match(dst,pattern)
    bg = cv2.imread("imgs/background3.jpg")
    cv2.rectangle(bg,(x,y),(x+pattern_col,y+pattern_row),(255,0,0))
    cv2.imshow("test",bg)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()