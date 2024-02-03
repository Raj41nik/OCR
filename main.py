import cv2
from PIL import Image
import pytesseract

camera = cv2.VideoCapture(0)

while True:
    _,image=camera.read()
    cv2.imshow('Text detection',image)
    if cv2.waitKey(1)& 0xFF==ord('s'):
        cv2.imwrite('test1.jpg',image)
        break

camera.release()
cv2.destroyAllWindows()

def tesseract():
    path_to_tessearct=r"/opt/local/bin/tesseracts"
    imagepath="test1.jpg"
    pytesseract.tesseract_cmd=path_to_tessearct
    text=pytesseract.image_to_string(Image.open(imagepath))
    print(text)
tesseract()