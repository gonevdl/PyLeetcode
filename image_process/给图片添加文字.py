import cv2 as cv

img = cv.imread("./src/2d6eb26d900a4631817007b08e7bf93e_cropped.jpg")
text = "hello world"
font = cv.FONT_HERSHEY_PLAIN
text_img = cv.putText(img, text, (400, 1000), font, 2, (0, 0, 255), 2)
cv.imwrite("./src/2d6eb26d900a4631817007b08e7bf93e_cropped_text.jpg", text_img)
