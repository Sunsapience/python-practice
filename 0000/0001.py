from PIL import Image, ImageDraw, ImageFont


def img_addnum(img_name, num):
    im = Image.open(img_name)
    draw = ImageDraw.Draw(im)

    #width and height
    w = im.width;
    h = im.height;
    print( h, w)
    
    #load font
    #fnt = ImageFont.load_default()
    fnt = ImageFont.truetype('arial.ttf', int(h * 0.15))

    
    draw.text((w * 0.91 , h * 0.01), num, font=fnt, fill='red')
    im.save(img_name.split('.')[0] + '2.jpg')

if __name__ == '__main__':
    img_addnum('C:/Users/wlgzg/Desktop/Corong.jpg', '3')