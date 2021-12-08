"""
第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片
"""
# 验证码不够具有混淆性，代码可以再完善


from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string

# 定义整体图片的高和宽
height = 100
width = 200


# 生成一个随机字符串，是26个大写字母和10个数字，字符穿长度由外部来定
def randString(number):
    rand_str = ""
    seed_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    seed_low = seed_up.lower()
    seed_num = "0123456789"
    seed = seed_num + seed_low + seed_up
    for i in range(0, number):
        rand_ch = random.randint(0, 61)
        rand_str += seed[rand_ch]
    return rand_str


# 生成随机颜色
def randColor():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# 生成随机的高和宽
def randHightAndWight():
    return random.randint(0, width), random.randint(0, height)


# 创建一张图片，并将生成的随机颜色的随机字符串写入图片
def createImage():
    # 生成一张新图片
    img = Image.new(mode='RGB', size=(width, height), color=(randColor()))
    font = ImageFont.truetype("./src/simsun.ttc", 80)  # 验证码的字体
    # 创建画笔
    draw = ImageDraw.Draw(img)
    # 生成字符串
    text = randString(4)
    draw.text((30, 10), text, fill=randColor(), font=font, spacing=5)
    drawLines(draw)
    draw = addPoint(draw)
    return img


# 绘制干扰线
def drawLines(draw: ImageDraw.Draw):
    """
    :param draw: ImageDraw.Draw()
    :param width:
    :param height:
    :return:
    """
    # 添加20条线
    for i in range(0, 20):
        # draw = ImageDraw.Draw(img)
        begin = randHightAndWight()
        end = randHightAndWight()
        draw.line([begin, end], fill=randColor())


# 创建扭曲，加入滤镜
def final(img):
    # img = Image.new()
    # 创建扭曲
    # img = img.transform((width + 20), (height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1), Image.BILINEAR)
    # 加入滤镜
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，加强边界
    img = img.filter(ImageFilter.BLUR)
    return img


# 添加干扰点
def addPoint(draw):
    # draw = ImageDraw.Draw()
    # 添加100个干扰点
    for i in range(0, 500):
        x, y = randHightAndWight()
        draw.point((x, y), fill=randColor())
        # draw.point((x, y), fill=(0, 0, 255))
    return draw


if __name__ == '__main__':
    img = createImage()
    img = final(img)
    img.save("./src/yanzhengma.jpg")
