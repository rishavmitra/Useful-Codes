'''from PIL import Image

img = Image.open("PassportSize.jpeg")

img2 = img.transpose(Image.FLIP_LEFT_RIGHT)

img2.save('Flipped.png')

img2.show()'''

import cv2

img = cv2.imread('Flipped.png')

clahe = cv2.createCLAHE()

#converting to grayscale

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

en_img = clahe.apply(gray_img)

cv2.imwrite('Enhanced_Flipped.png',en_img)

cv2.imshow('Image',en_img)

cv2.waitKey(0)

cv2.destroyAllWindows()

