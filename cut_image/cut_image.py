# _*_  coding: utf-8 _*_

from PIL import Image
import sys

#将图片填充为正方形
def fill_image(image):
    width, height = image.size
    #以图片宽高最大值作为边长生成正方形白底背景
    #if width > height:
    #    bg_length = width
    #else:
    #    bg_length = height
    bg_length = width if width > height else height #和上面注释掉的功能是一样的写起来更方便
    new_image = Image.new(image.mode, (bg_length, bg_length), color='white')
    #将要切的图粘贴在背景中间
    if width > height: #宽大于高竖向粘贴在背景中间坐标(X1,0)
        new_image.paste(image, (0, int((bg_length - height) / 2)))
    else: #高大于宽横向粘贴在背景中间坐标(0,y1)
        new_image.paste(image, (int((bg_length - width) / 2, 0)))
    return new_image

#将图片切成9块
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    #切图按照(left, upper, right, lower)定位来切
    for i in range(0, 3):
        for j in range(0, 3):
            #先横着切再竖着切
            print('定位参数：')
            print((j*item_width, i*item_width, (j+1)*item_width, (i+1)*item_width))
            box = (j*item_width, i*item_width, (j+1)*item_width, (i+1)*item_width)
            box_list.append(box)
    #按定位参数切图
    image_list = [image.crop(box) for box in box_list]
    return image_list

#保存
def save_images(image_list):
    index = 1
    name = input('请输入保存名称：')
    for image in image_list: #逐个保存为png格式小图
        image.save('./save/' +name + str(index) + '.png', 'PNG')
        index += 1
    return print('处理完成！')

if __name__ == '__main__':
    file_path = input('处理图片名称：') + '.' + input('处理图片格式：')
    image = Image.open('./pics/' + file_path)
    image.show()
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list)

#以上