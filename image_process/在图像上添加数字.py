import cv2 as cv

img = cv.imread("./src/beach-5264739.jpg")
print(img.shape)
text = "hello world"
img_text = cv.putText(img, text, (1000, 1000), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=10,
                      color=(0, 0, 255), thickness=2)
cv.imwrite("./src/beach-5264739-result.jpg", img_text)
