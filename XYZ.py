'''
Created on May 26, 2016


@author: Jonathan Muckell, Ph.D.
@license: GNU General Public License v3.0

Users are encouraged to use, modify and extend this work under the GNU GPLv3 license.

Please cite the following paper to provide credit to this work:

Jonathan Muckell, Yuchi Young, and Mitch Leventhal. 2017. 
A Wearable Motion Tracking System to Reduce Direct Care Worker Injuries: An Exploratory Study. 
In Proceedings of DH ’17, London, United Kingdom, July 02-05, 2017, 5 pages.
DOI: hp://dx.doi.org/10.1145/3079452.3079493

-------------
'''

import math


class XYZ:
 
    def __init__(self,l):
        self.x = float(l[0])
        self.y = float(l[1])
        self.z = float(l[2])        
        

    @staticmethod
    def getDistanceBetweenPoints(p1, p2):
        distance = math.sqrt( (p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2 )
        return distance


    # https://www.mathsisfun.com/algebra/trig-cosine-law.html
    @staticmethod
    def getAngleOfTriangle(a,b,c):

        #math.acos(0) # returns in radians
        numerator = c**2 - a**2 - b**2 
        denominator = -2*a*b
        # print("numerator: ",numerator)
        # print("denominator: ",denominator)
        
        radians = math.acos(numerator / denominator)
        degrees = math.degrees(radians)
        #print("degrees",degrees)
        return degrees


    @staticmethod
    def getVector(pt1, pt2):
        # FROM: http://tutorial.math.lamar.edu/Classes/CalcII/Vectors_Basics.aspx
        x = pt2.x - pt1.x
        y = pt2.y - pt1.y
        z = pt2.z - pt1.z
        vector = XYZ([x, y, z])
        # print("get Vector = ", x, " | ", y, " | ", z)
        return vector
        
 
    @staticmethod       
    def crossProduct(a, b):
        # Equation from # http://tutorial.math.lamar.edu/Classes/CalcII/CrossProduct.aspx#Vectors_CrossProd_Ex2
        x = (a.y * b.z) - (a.z * b.y)
        y = (a.z * b.x) - (a.x * b.z)
        z = (a.x * b.y) - (a.y * b.x)
        vector = XYZ([x, y, z])
#        print("cross product = ", x, " | ", y, " | ", z)
        return vector
 
    @staticmethod
    def getPlaneNormal(P,Q,R):
        # http://tutorial.math.lamar.edu/Classes/CalcIII/EqnsOfPlanes.aspx
        PQ = XYZ.getVector(P,Q)
        PR = XYZ.getVector(P,R)
        normal = XYZ.crossProduct(PQ, PR)
        return normal
        

    @staticmethod
    def getMidpoint(pt1, pt2):
        x = (pt1.x + pt2.x) / 2
        y = (pt1.y + pt2.y) / 2
        z = (pt1.z + pt2.z) / 2
        return XYZ([x, y, z])


    @staticmethod  
    def testNormal():
        P = XYZ([1, -2, 0])
        Q = XYZ([3, 1, 4])
        R = XYZ([0, -1, 2])
        normal = XYZ.getPlaneNormal(P, Q, R)
#        print("normal = ", normal.x, " | ", normal.y, " | ", normal.z)
        
        a = XYZ([2, 1, -1])
        b = XYZ([-3, 4, 1])
        XYZ.crossProduct(a, b)
        

XYZ.testNormal()

