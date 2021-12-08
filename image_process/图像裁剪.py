import cv2 as cv

img = cv.imread("./src/2d6eb26d900a4631817007b08e7bf93e.jpg")
print(img.shape)
cropped = img[0:1200, 0:2400]
cv.imwrite("./src/2d6eb26d900a4631817007b08e7bf93e_cropped.jpg", cropped)