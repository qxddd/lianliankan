# -*- coding: utf-8 -*-
#point[0]是纵坐标
#point[1]是横坐标
class findsolution:

    def __init__(self, position):
        self.position = position

    def noturn(self, point1, point2):

        #判断两点是否是直连
        if point1[0] != point2[0] and point1[1] != point2[1]:
            return False
        #minpoint = [0, 0]
        #maxpoint = [0, 0]

        #如果是横线连接
        if point1[0] == point2[0]:
            if point1[1] > point2[1]:
                maxpoint = list(point1)
                minpoint = list(point2)
            else:
                maxpoint = list(point2)
                minpoint = list(point1)
            while minpoint[1] < maxpoint[1]:
                minpoint[1] = minpoint[1] + 1
                if minpoint == maxpoint:
                    return True
                elif self.position[minpoint[0]][minpoint[1]] == 0:
                    continue
                elif self.position[minpoint[0]][minpoint[1]] == self.position[maxpoint[0]][maxpoint[1]]:
                    return True
                else:
                    return False
        #如果是竖线连接
        else:
            if point1[0] > point2[0]:
                maxpoint = list(point1)
                minpoint = list(point2)
            else:
                maxpoint = list(point2)
                minpoint = list(point1)
            while minpoint[0] < maxpoint[0]:
                minpoint[0] = minpoint[0] + 1
                if minpoint == maxpoint:
                    return True
                elif self.position[minpoint[0]][minpoint[1]] == 0:
                    continue
                elif self.position[minpoint[0]][minpoint[1]] == self.position[maxpoint[0]][maxpoint[1]]:
                    return True
                else:
                    return False
        '''
        return point1, point2
        '''

    #判断两点是否是一个转折点连接
    def oneturn(self, point1, point2):
        #定义围成的那个矩形的另外两个点
        a1 = [0,0]
        a2 = [0,0]
        #获取这两个点的坐标
        a1[0] = int(point1[0])
        a1[1] = int(point2[1])
        a2[0] = int(point2[0])
        a2[1] = int(point1[1])
        #判断a1,a2两点是否为空，如果都不为空说明无法消除
        if self.position[a1[0]][a1[1]] != 0 and self.position[a2[0]][a2[1]] != 0:
            return False

        #如果a1为空
        if self.position[a1[0]][a1[1]] == 0:
            self.position[a1[0]][a1[1]] = self.position[point1[0]][point1[1]]
            #测试a1与point1，a1与point2是否连通
            if self.noturn(a1, point1) and self.noturn(a1, point2):
                self.position[a1[0]][a1[1]] = 0
                return True
            else:
                self.position[a1[0]][a1[1]] = 0
                return False

        #如果a2为空
        else:
            self.position[a2[0]][a2[1]] = self.position[point1[0]][point1[1]]
            #测试a2与point1，a2与point2是否连通
            if self.noturn(a2, point1) and self.noturn(a2, point2):
                self.position[a2[0]][a2[1]] = 0
                return True
            else:
                self.position[a2[0]][a2[1]] = 0
                return False
    #判断两点是否为两个转折点连通
    def twoturn(self,point1, point2):
        tmp = list(point1)
        #往上查询
        if point1[0] > 0:
            for i in range(point1[0]):
                tmp[0] = tmp[0] - 1
                if self.position[tmp[0]][tmp[1]] == 0:
                    if self.oneturn(tmp, point2):
                        return True
                else:
                    break
        #往下查询
        elif point1[0] < 11:
            for i in range(point1[0]):
                tmp[0] = tmp[0] + 1
                if self.position[tmp[0]][tmp[1]] == 0:
                    if self.oneturn(tmp, point2):
                        return True
                else:
                    break
        #往左查询
        elif point1[1] > 0:
            for i in range(point1[1]):
                tmp[1] = tmp[1] - 1
                if self.position[tmp[0]][tmp[1]] == 0:
                    if self.oneturn(tmp, point2):
                        return True
                else:
                    break
        #往右查询
        elif point1[1] < 11:
            for i in range(point1[1]):
                tmp[1] = tmp[1] + 1
                if self.position[tmp[0]][tmp[1]] == 0:
                    if self.oneturn(tmp, point2):
                        return True
                else:
                    break
        else:
            return False
    #如果成功消除，设置两点为0
    def setzero(self, point1, point2):
        self.position[point1[0]][point1[1]] = 0
        self.position[point2[0]][point2[1]] = 0
    #更新position
    def returnposition(self):
        return self.position