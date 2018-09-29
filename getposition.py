#-*- coding:utf-8 -*-
import cv2
import time
import findsolution
# 获取图片哈希值
def dHash(img):
    # 生成缩略图
    img = cv2.resize(img,(9,8),interpolation=cv2.INTER_CUBIC)
    # 获取灰度图
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hash_str = ''
    # 生成哈希
    for i in range(8):
        for j in range(8):
            if gray[i,j] > gray[i,j+1]:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str

# 计算两张图片的哈希值差异
def cmpHash(hash1,hash2):
    n = 0
    if len(hash1) != len(hash2):
        return -1

    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            n = n + 1
    return n

# 截取动物的区域
def getcrop(x1,x2,y1,y2,img):
    #img = cv2.imread(r"tmp/demo.png")
    cropimg = img[y1:y2,x1:x2]
    return cropimg
    #print y1,y2,x1,x2

# 判断每个位置的动物种类，并把信息存到一个二维列表中
def getposition(img):

    position = [[0 for i in range(9)] for j in range(12)]
    gou = "0000000001101011100101110101010101010101011100010100110101001100"
    hema = "0011100000110110001100110101010101011101010100010110000100000000"
    ji = "0001000000010000010101000001001010010110000101100100100101101000"
    mao = "1000010001110001011010111001011100010111001101111010101001000000"
    mogui = "1000001001010101110001001001001010100010001100100110100100110000"
    tuzi = "0000000001010101010101110101011000110011001100111001011000000001"
    wa = "0101000001110001011011010000110101110001010000110100110100000000"
    zhu = "1000000001001101101010100110101101101001001110011101110001010000"
    #img = cv2.imread(r"tmp/demo.png")
    x = 55
    y = 364
    for i in range(1,11):
        for j in range(1,8):
            x1 = x + 140*(j - 1)
            x2 = x1 + 132
            y1 = y + 140*(i - 1)
            y2 = y1 + 132
            cropimg = getcrop(x1,x2,y1,y2,img)
            hash_str = dHash(cropimg)
            if cmpHash(hash_str,gou) < 10:
                position[i][j] = 1
            elif cmpHash(hash_str,hema) < 10:
                position[i][j] = 2
            elif cmpHash(hash_str,ji) < 10:
                position[i][j] = 3
            elif cmpHash(hash_str,mao) < 10:
                position[i][j] = 4
            elif cmpHash(hash_str,mogui) < 10:
                position[i][j] = 5
            elif cmpHash(hash_str,tuzi) < 10:
                position[i][j] = 6
            elif cmpHash(hash_str,wa) < 10:
                position[i][j] = 7
            else:
                position[i][j] = 8
    return position

#寻找相同的动物位置
def getthesame(position):
    for i in range(1, 11):
        for j in range(1, 8):
            if position[i][j] != 0:
                for x in range(1, 11):
                    for y in range(1, 8):
                        if x == i and y == j:
                            continue
                        elif position[i][j] == position[x][y]:
                            point1 = [i, j]
                            point2 = [x, y]
                            yield point1, point2
                        else:
                            pass


if __name__ == '__main__':
    start = time.time()
    img = cv2.imread(r"tmp/demo2.png")
    position = getposition(img)
    answer = findsolution.findsolution(position)

    for m, n in getthesame(position):
        if answer.noturn(m, n):
            answer.setzero(m, n)
    for a, s in getthesame(answer.returnposition()):
        if answer.oneturn(a, s):
            answer.setzero(a, s)
    for a, s in getthesame(answer.returnposition()):
        if answer.oneturn(a, s):
            answer.setzero(a, s)
    for a, s in getthesame(answer.returnposition()):
        if answer.twoturn(a, s):
            answer.setzero(a, s)
    for a, s in getthesame(answer.returnposition()):
        if answer.twoturn(a, s):
            answer.setzero(a, s)
    for a, s in getthesame(answer.returnposition()):
        if answer.noturn(a, s):
            answer.setzero(a, s)
    for a, s in getthesame(answer.returnposition()):
        if answer.oneturn(a, s):
            answer.setzero(a, s)
    for a, s in getthesame(answer.returnposition()):
        if answer.twoturn(a, s):
            answer.setzero(a, s)
    for i in range(12):
        print answer.returnposition()[i]

    end = time.time()
    print('Running time: %s Seconds' % (end - start))

