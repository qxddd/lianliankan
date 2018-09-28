# -*- coding: utf-8 -*-

class findsolution(object):

    def __init__(self, position):
        self.position = position

    def noturn(self, point1, point2):
        #判断两点是否是直连
        if point1[0] != point2[0] or point1[1] != point2[1]:
            return False
        minpoint = [0, 0]
        maxpoint = [0, 0]

        #如果是横线连接
        if point1[0] == point2[0]:
            if point1[1] > point2[1]:
                maxpoint = point1
                minpoint = point2
            else:
                maxpoint = point2
                minpoint = point1
            while minpoint[1] <= maxpoint[1]:
                minpoint[1] = minpoint[1] + 1
                if self.position[minpoint[0]][minpoint[1]] != 0:
                    return False
        #如果是竖线连接
        else:
            if point1[0] > point2[0]:
                maxpoint = point1
                minpoint = point2
            else:
                maxpoint = point2
                minpoint = point1
            while minpoint[0] <= maxpoint[0]:
                minpoint[0] = minpoint[0] + 1
                if self.position[minpoint[0]][minpoint[1]] != 0:
                    return False

    #判断两点是否是一个转折点连接
    def oneturn(self,point1,point2):
