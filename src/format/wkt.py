import sys
import json
sys.path.append("..")
from util.dataType import typeof


class wktHelper:
    #坐标串转wkt
    def coordinatesToWKT(self,coordinates):
        try:
            wkt='('
            depth=1
            if typeof(coordinates)=='list':
                if typeof(coordinates[0])=='list':
                    if typeof(coordinates[0][0])=='list':
                        if typeof(coordinates[0][0][0])=='list':
                            if typeof(coordinates[0][0][0][0])=='list':
                                return ''
                            else:
                                depth=4
                        else:
                            depth=3
                    else:
                        depth=2
                else:
                    depth=1
            else:
                return ''
            if depth==1:
                wkt += str(coordinates[0]) +' '+ str(coordinates[1])
            elif depth==2:
                for i in range(len(coordinates)):
                    wkt += str(coordinates[i][0]) +' '+ str(coordinates[i][1])
                    if i!=len(coordinates)-1:
                        wkt+=','
            elif depth==3:
                for i in range(len(coordinates)):
                    wkt += '('
                    for j in range(len(coordinates[i])):
                        wkt += str(coordinates[i][j][0]) +' '+ str(coordinates[i][j][1])
                        if j!=len(coordinates[i])-1:
                            wkt+=','
                    wkt += ')'
                    if i!=len(coordinates)-1:
                        wkt+=','
            elif depth==4:
                for i in range(len(coordinates)):
                    wkt += '('
                    for j in range(len(coordinates[i])):
                        wkt += '('
                        for k in range(len(coordinates[i][j])):
                            wkt += str(coordinates[i][j][k][0])+' '+str(coordinates[i][j][k][1])
                            if k!=len(coordinates[i][j])-1:
                                wkt+=','
                        wkt += ')'
                        if j!=len(coordinates[i])-1:
                            wkt+=','
                    wkt += ')'
                    if i!=len(coordinates)-1:
                        wkt+=','
            wkt +=')'
            return wkt
        except Exception as err:
            return ''
    #wkt转坐标串
    def wktToCoordinates(self,wktstr):
        try:
            wktstr=wktstr.upper()
            if wktstr.startswith("POINT")==True:
                firstLeftIndex = wktstr.index('(')
                coorstr = wktstr[firstLeftIndex+1:len(wktstr)-1]
                ringsArray = coorstr.strip().split(" ")
                return [float(ringsArray[0]),float(ringsArray[1])]
            elif wktstr.startswith("MULTIPOINT")==True:
                firstLeftIndex = wktstr.index('(')
                coorstr = wktstr[firstLeftIndex+1:len(wktstr)-1]
                rArray=[]
                pointArr=coorstr.split(",")
                for k in range(0,len(pointArr)):
                    pt_arr=pointArr[k].strip().split(" ")
                    rArray.append([float(pt_arr[0]),float(pt_arr[1])])
                return rArray
            elif wktstr.startswith("LINESTRING")==True:
                firstLeftIndex = wktstr.index('(')
                coorstr = wktstr[firstLeftIndex+1:len(wktstr)-1]
                rArray=[]
                pointArr=coorstr.split(",")
                for k in range(0,len(pointArr)):
                    pt_arr=pointArr[k].strip().split(" ")
                    rArray.append([float(pt_arr[0]),float(pt_arr[1])])
                return rArray
            elif wktstr.startswith("MULTILINESTRING")==True:
                firstLeftIndex = wktstr.index('(')
                coorstr = wktstr[firstLeftIndex+1:len(wktstr)-1]
                rArray=[]
                coorstr=coorstr.replace("), (","),(")
                ringsArray = coorstr.split("),(")
                for j in range(0,len(ringsArray)):
                    ringStr=ringsArray[j]
                    if(len(ringsArray)==1):
                        ringStr=ringStr[1:len(ringStr)-1]
                    elif j==0:
                        ringStr=ringStr.replace('(','')
                    elif j==(len(ringsArray)-1):
                        ringStr=ringStr[0:len(ringStr)-1]
                    ptsArray=[]
                    pointArr=ringStr.split(",")
                    for k in range(0,len(pointArr)):
                        pt_arr=pointArr[k].strip().split(" ")
                        ptsArray.append([float(pt_arr[0]),float(pt_arr[1])])
                    rArray.append(ptsArray)
                return rArray
            elif wktstr.startswith("POLYGON")==True:
                firstLeftIndex = wktstr.index('(')
                coorstr = wktstr[firstLeftIndex+1:len(wktstr)-1]
                rArray=[]
                coorstr=coorstr.replace("), (","),(")
                ringsArray = coorstr.split("),(")
                for j in range(0,len(ringsArray)):
                    ringStr=ringsArray[j]
                    if(len(ringsArray)==1):
                        ringStr=ringStr[1:len(ringStr)-1]
                    elif j==0:
                        ringStr=ringStr.replace('(','')
                    elif j==(len(ringsArray)-1):
                        ringStr=ringStr[0:len(ringStr)-1]
                    ptsArray=[]
                    pointArr=ringStr.split(",")
                    for k in range(0,len(pointArr)):
                        pt_arr=pointArr[k].strip().split(" ")
                        ptsArray.append([float(pt_arr[0]),float(pt_arr[1])])
                    rArray.append(ptsArray)
                return rArray
            elif wktstr.startswith("MULTIPOLYGON")==True:
                firstLeftIndex = wktstr.index('(')
                coorstr = wktstr[firstLeftIndex+1:len(wktstr)-1]
                pArray=[]
                coorstr=coorstr.replace(")), ((",")),((")
                polygonArray = coorstr.split(")),((")
                for i in range(0,len(polygonArray)):
                    pStr=polygonArray[i]
                    if len(polygonArray)==1:
                        pStr=pStr[1:len(pStr)-1]
                    elif i==0:
                        pStr=pStr[1:len(pStr)]+")"
                    elif i==(len(polygonArray)-1):
                        pStr="("+pStr[0:len(pStr)-1]
                    else:
                        pStr="("+pStr+")"
                    rArray=[]
                    pStr=pStr.replace("), (","),(")
                    ringsArray = pStr.split("),(")
                    for j in range(0,len(ringsArray)):
                        ringStr=ringsArray[j]
                        if(len(ringsArray)==1):
                            ringStr=ringStr[1:len(ringStr)-1]
                        elif j==0:
                            ringStr=ringStr.replace('(','')
                        elif j==(len(ringsArray)-1):
                            ringStr=ringStr[0:len(ringStr)-1]
                        ptsArray=[]
                        pointArr=ringStr.split(",")
                        for k in range(0,len(pointArr)):
                            pt_arr=pointArr[k].strip().split(" ")
                            ptsArray.append([float(pt_arr[0]), float(pt_arr[1])])
                        rArray.append(ptsArray)
                    pArray.append(rArray)
                return pArray
        except Exception as err:
            return []

wkthelper = wktHelper()
# print(wkthelper.wktToCoordinates('POINT(6 10)'))
# print(wkthelper.wktToCoordinates('MULTIPOINT(3.5 5.6, 4.8 10.5)'))
# print(wkthelper.wktToCoordinates('LINESTRING(3 4,10 50,20 25)'))
# print(wkthelper.wktToCoordinates('MULTILINESTRING((3 4,10 50,20 25),(-5 -8,-10 -8,-15 -4))'))
# print(wkthelper.wktToCoordinates('POLYGON((1 1,5 1,5 5,1 5,1 1),(2 2,2 3,3 3,3 2,2 2))'))
# print(wkthelper.wktToCoordinates('MULTIPOLYGON(((1 1,5 1,5 5,1 5,1 1),(2 2,2 3,3 3,3 2,2 2)),((6 3,9 2,9 4,6 3)))'))
# print(wkthelper.coordinatesToWKT([6,10]))
# print(wkthelper.coordinatesToWKT([[3,4],[10,50],[20,25]]))
# print(wkthelper.coordinatesToWKT([[[1,1],[5,1],[5,5],[1,5],[1,1]],[[2,2],[2,3],[3,3],[3,2],[2,2]]]))
# print(wkthelper.coordinatesToWKT([[[[1,1],[5,1],[5,5],[1,5],[1,1]],[[2,2],[2,3],[3,3],[3,2],[2,2]]],[[[6,3],[9,2],[9,4],[6,3]]]]))

