import sys
sys.path.append("..")
from proj.transform import Yproj

from geometry import Geometry

class Point(Geometry):
    #定义基本属性
    x=0
    y=0
    gettype = 'Point'
    wkid = 4326
    #定义私有属性,私有属性在类外部无法直接进行访问
    __coordinates = []
    #定义构造方法
    def __init__(self,coordinates,wkid=4326):
        self.x=coordinates[0]
        self.y=coordinates[1]
        self.wkid=wkid
        self.__coordinates = [self.x,self.y]
    def getGeoType(self):
        return self.__gettype
    def transform(self,wkid):
        proj=Yproj(self.wkid,wkid)
        self.x,self.y=proj.transform(self.x,self.y)
        self.__coordinates = [self.x,self.y]
        self.wkid=wkid
        return self
    def translate(self,x,y):
        self.x=self.x+x
        self.y=self.y+y
        self.__coordinates = [self.x,self.y]
        return self
    def getExtent(self):
        return [self.x,self.y,self.x,self.y]
    def getCoordinates(self):
        return self.__coordinates

point=Point([2,3])
print(point.transform(3857))
