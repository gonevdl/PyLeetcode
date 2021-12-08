"""
第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""
import os

import cv2 as cv

cuDdir = os.curdir  # 获取当前python的文件夹
sourceDir = os.path.join(cuDdir, "src/img")
desDir = os.path.join(cuDdir, "src/img_resized")


def resizeBatch(sourDir, desDir):
    img_list = os.listdir(sourDir)

    for img in img_list:
        pic = cv.imread(os.path.join(sourDir, img), cv.IMREAD_COLOR)
        pic_resized = cv.resize(pic, (pic.shape[1] // 4, pic.shape[0] // 4))
        cv.imwrite(os.path.join(desDir, img), pic_resized)
        print(img + "输出成功！")
        # print(type(img))
        # break


if __name__ == "__main__":
    resizeBatch(sourceDir, desDir)
