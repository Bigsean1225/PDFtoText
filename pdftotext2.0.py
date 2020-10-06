import pdf2image
from PIL import Image
import time
import sys
import pytesseract

location = input("PDF Location : ")
output = input("Output Folder : ")
name = input("Name of Output : ")
numberofpages = input("Number of Pages : ")
DPI = input("DPI : ")

FIRST_PAGE = None
LAST_PAGE = None
FORMAT = 'jpg'
THREAD_COUNT = 16
USERPWD = None
USE_CROPBOX = False
STRICT = False

def pdftopil():

    start_time = time.time()
    pil_images = pdf2image.convert_from_path(location, dpi=DPI, output_folder=output, first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)
    print ("Time taken : " + str(time.time() - start_time))
    return pil_images
    
def save_images(pil_images):
    index = 1
    for image in pil_images:
        image.save(str(name) + str(index) + ".jpg")
        index += 1

if __name__ == "__main__":
    pil_images = pdftopil()
    save_images(pil_images)
    pytesseract.pytesseract.tesseract_cmd ='/Users/sdock/Documents/tesseract/4.1.1/bin/tesseract'
    scanning = True
    while scanning:
        scanner = 1
        text = pytesseract.image_to_string('/Users/sdock/Desktop/' + str(name) + str(scanner) + ".jpg")
        print(text)
        text_file = open(str(name) + ".txt","w+")
        text_file.write(text)
        text_file.close()
        scanner += 1
        scanning = False
        #
    scanningmulti = True
    while scanningmulti:
        if scanner != int(numberofpages):
            text = pytesseract.image_to_string('/Users/sdock/Desktop/' + str(name) + str(scanner) + ".jpg")
            print(text)
            text_file = open(str(name) + ".txt","a")
            text_file.write(text)
            text_file.close()
            scanner += 1
        if scanner == int(numberofpages):
            text = pytesseract.image_to_string('/Users/sdock/Desktop/' + str(name) + str(numberofpages) + ".jpg")
            print(text)
            text_file = open(str(name) + ".txt","a")
            text_file.write(text)
            text_file.close()
            scanningmulti = False
