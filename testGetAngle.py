
import math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


def getAngle(self, center, p1, p2)
    dx1 = p1.x() - center.x();
    dy1 = p1.y() - center.y();

    dx2 = p2.x() - center.x();
    dy2 = p2.y() - center.y();

    c = math.sqrt(dx1*dx1 + dy1*dy1) * math.sqrt(dx2*dx2 + dy2*dy2)
    if c == 0 return 0
    angle = math.acos((dx1*dx2+dy1*dy2)/c)
    
    return angle