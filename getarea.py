from PIL import Image

def contrastimg(img, box, name):
    cropimg = img.crop(box)
    cropimg.save(r"tmp/" + name + ".png")

if __name__ == '__main__':
    img1 = Image.open(r"tmp/demo.png")
    #img2 = Image.open(r"tmp/demo2.png")
    box1 = (195,1064,327,1196)
    #box2 = (54,504,186,635)
    contrastimg(img1, box1, "tuzi")
    #contrastimg(img2, box1, "cropimg3")