import cv2


# import test

def dHash(img):
    img = cv2.resize(img, (9, 8), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hash_str = ''
    for i in range(8):
        for j in range(8):
            if gray[i, j] > gray[i, j + 1]:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str

'''
def cmpHash(hash1, hash2):
    n = 0
    if len(hash1) != len(hash2):
        return -1

    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            n = n + 1
    return n
'''

img1 = cv2.imread(r"tmp/zhu.png")
# img2 = cv2.imread(r"tmp/gou.png")
# img2 = test.getcrop(364,496,55,187)
hash1 = dHash(img1)
# hash1 = "0001000000010000010101000001001010010110000101100100100101101000"
# hash2 = dHash(img2)
print(hash1)
# print(hash2)
# x = cmpHash(hash1,hash2)
# print(x)
