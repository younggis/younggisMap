import abc

class Geometry(metaclass=abc.ABCMeta):
    @abc.abstractmethod #获取几何类型
    def getGeoType(self):
        pass
    @abc.abstractmethod #坐标系转换
    def transform(self):
        pass
    @abc.abstractmethod #平移
    def translate(self):
        pass
    @abc.abstractmethod #获取几何范围
    def getExtent(self):
        pass
    @abc.abstractmethod #获取坐标
    def getCoordinates(self):
        pass