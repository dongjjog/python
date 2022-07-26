import numpy as np
from stl import mesh
from scipy.spatial import ConvexHull
import pyvista as pv
from pyvista import PolyData
import random

p=0
Q=[]
while p<50:
    a=np.random.uniform(0,2*np.pi)  #0~2pi까지 100개로 쪼갠다
    b=np.random.uniform(0,np.pi)
    x=np.random.uniform(1,2)*np.outer(np.cos(a),np.sin(b))  # 외적계산
    y=np.random.uniform(1,2)*np.outer(np.sin(a),np.sin(b))
    z=np.random.uniform(1,2)*np.outer(np.ones(np.size(a)),np.cos(b))
    p=p+1

    xlist_all = x
        #file.write("x, y, z\n")
    for i, xlist1 in enumerate(xlist_all):
        for j, xvalue in enumerate(xlist1): 
            xvalue = x[i][j]  
            yvalue = y[i][j]
            zvalue = z[i][j]
            Q.append([xvalue,yvalue,zvalue])
    
K=np.array(Q)
#print(K)


def polyhull(X,Y,Z):
    hull=ConvexHull(np.column_stack((X, Y, Z)))
    faces=np.column_stack((3*np.ones((len(hull.simplices), 1), dtype=np.int), hull.simplices)).flatten()
    poly=PolyData(hull.points, faces)
    return poly
X,Y,Z=K.T
hull=polyhull(X,Y,Z)
hull.plot()
#hull.plot(show_edges=True) 
hull.save('ellipsoid.stl')



#convexhull(point):블록껍질을 구성할 point의 좌표
#numpy.column_stack(tup):일련의 1차원 배열을 가져와 열로 쌓아 단일 2차원 배열을 만듭니다. 2차원 배열은 와 마찬가지로 있는 그대로 쌓입니다
#flatten(): 평면화를 만든다, 병합하는것
#polydata(point,faces):빈 메쉬를 만든다.