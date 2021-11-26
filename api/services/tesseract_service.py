import cv2
import pytesseract
import os


class OCR_Service:
    def __init__(self):
        pass


# convert default BGR to grayscale image
def convert_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# convert default BGR to RGB image
def bgr_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def extract_content(img):
    return ''


if __name__ == "__main__":
    ocr_object = OCR_Service()
    img_path = os.path.join('/media/images/test.jpg')
    img = cv2.imread(img)
