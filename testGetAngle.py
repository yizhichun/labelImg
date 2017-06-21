
import math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np

def getAngle(center, p1, p2):
    dx1 = p1.x() - center.x();
    dy1 = p1.y() - center.y();

    dx2 = p2.x() - center.x();
    dy2 = p2.y() - center.y();

    c = math.sqrt(dx1*dx1 + dy1*dy1) * math.sqrt(dx2*dx2 + dy2*dy2)
    if c == 0: return 0
    print("dx1:%d,dx2:%d,dy1:%d,dy2:%d,c:%lf" % (dx1,dx2,dy1,dy2,c))
    y = (dx1*dx2+dy1*dy2)/c
    print(y)
    angle = math.acos(y)

    if (dx1*dy2-dx2*dy1)>0:   
    	return angle
    else:
    	return -angle

def getSymmetricalPoint(theta, p1, p2):
    center = (p1 + p2) / 2
    a = math.tan(theta)
    b = center.y() - a * center.x()
    X3 = p1.x() - 2*a*(a*p1.x()-p1.y()+b) / (a*a+1)
    Y3 = p1.y() + 2*(a*p1.x()-p1.y()+b) / (a*a+1)
    X4 = p2.x() - 2*a*(a*p2.x()-p2.y()+b) / (a*a+1)
    Y4 = p2.y() + 2*(a*p2.x()-p2.y()+b) / (a*a+1)

    p3 = QPointF(X3, Y3)
    p4 = QPointF(X4, Y4)
    return p3, p4


if __name__ == '__main__':

    theta = math.pi/4;
    p1=QPointF(1,0)
    p2 = QPointF(-1,0)
    p3,p4 = getSymmetricalPoint(theta,p1,p2)
    print(p1)
    print(p3)
    print(p2)
    print(p4)

    # center = QPointF(0,0)
    # p1 = QPointF(1,1)
    # p2 = QPointF(1,0)
    # print((p1+p2)/2)
    # angle = getAngle(center, p1, p2)
    # print(angle)


