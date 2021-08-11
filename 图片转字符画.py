from PIL import Image
import argparse

#构建命令行输入参数处理 ArgumentParser实例
parser = argparse.ArgumentParser()

# 定义输入文件、输出文件、输出字符画的宽和高
parser.add_argument('--file')     # 输入文件
parser.add_argument('-o','--output')    # 输出文件
parser.add_argument('--width',type = int,default = 150)      # 输出字符画宽
parser.add_argument('--height',type = int,default = 150)     # 输出字符画高

# 解析并获取参数
args = parser.parse_args()

# 输入的图片文件路径
IMG = args.file
# 输出字符画的宽度
WIDTH = args.width
# 输出字符画的高度
HEIGHT = args.height
# 输出字符画的路径
OUTPUT = args.output


# RGB值转字符函数
def get_char(r,g,b,alpha = 256):
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    if alpha == 0:
        return ' '
    # 获取字符集长度
    length = len(ascii_char)

    # 将RGB值转换为灰度值gray,灰度值范围为0-255
    gray= int(0.2126*r + 0.7152*g + 0.0722*b)

    # 灰度值范围0-255，字符集不足255个进行换算映射
    unit = (256.0+1)/length

    # 返回灰度值对应的字符
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    # 打开并调整图片的宽和高
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

    # 初始化输出的字符串
    txt = ''
    # 遍历图片中的每一行
    for i in range(HEIGHT):
        # 遍历该行中的每一列
        for j in range(WIDTH):
            # 将（j,i）坐标的RGB像素转为字符后添加到txt字符串
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open('output.txt','w') as f:
            f.write(txt)
        
