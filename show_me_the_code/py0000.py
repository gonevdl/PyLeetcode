import cv2 as cv

img = cv.imread("src/QQ1.jpg")
print(img.shape)
text = "99+"
font = cv.FONT_HERSHEY_PLAIN
img_text = cv.putText(img, text, (500, 100), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 255), thickness=2)
cv.imwrite("./src/QQ_modified.jpg", img_text)
