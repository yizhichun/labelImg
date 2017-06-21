
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



if __name__ == '__main__':
    center = QPointF(0,0)
    p1 = QPointF(1,1)
    p2 = QPointF(1,0)
    angle = getAngle(center, p1, p2)
    print(angle)


