'''
Created on May 27, 2016

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

from XYZ import XYZ
import math

class twistFrame:

    def __init__(self, leftShoulder, rightShoulder, leftHip, rightHip):
        self.leftShoulder  = leftShoulder
        self.rightShoulder = rightShoulder
        self.leftHip       = leftHip
        self.rightHip      = rightHip
    
    def getTwist(self):        
        hipOrigin = XYZ.getMidpoint(self.leftHip, self.rightHip)
        shoulderOrigin = XYZ.getMidpoint(self.leftShoulder, self.rightShoulder)
        translationVector = twistFrame.getTranslation(hipOrigin, shoulderOrigin)
        
        xt = self.leftShoulder.x + translationVector.x
        yt = self.leftShoulder.y + translationVector.y
        zt = self.leftShoulder.z + translationVector.z
        translated_Left_Shoulder = XYZ([xt, yt, zt])
        
        
        hipOrigin_LeftHip_Dist = XYZ.getDistanceBetweenPoints(self.leftHip, hipOrigin)
        hipOrigin_translated_Left_Shoulder_Dist = XYZ.getDistanceBetweenPoints(hipOrigin,translated_Left_Shoulder)
        LeftHip_translated_Left_Shoulder_Dist = XYZ.getDistanceBetweenPoints(self.leftHip, translated_Left_Shoulder)
        
        try:     
            angle = XYZ.getAngleOfTriangle(hipOrigin_LeftHip_Dist, hipOrigin_translated_Left_Shoulder_Dist, LeftHip_translated_Left_Shoulder_Dist)
        except ZeroDivisionError:
            print("WARNING - caught divide by zero error in getTwist method. Skipping data point.")
            return 0
        except ValueError:
            print("WARNING - caught ValueError in getTwist method. Skipping data point.")
            return 0            
        return angle
    
    
    def getTwist_OLD(self):        

        try:
            m1 = self.getLineSlope(self.leftShoulder, self.rightShoulder)
            c = self.getYIntersect(self.leftShoulder.x, self.leftShoulder.y, m1)
            m2 = self.getLineSlope(self.leftHip, self.rightHip)
            d = self.getYIntersect(self.leftHip.x, self.leftHip.y, m2)
            intersectPoint = self.getIntersectionOfTwoLines(m1, m2, c, d)
            # print("intersection point = ",intersectPoint.x," ",intersectPoint.y," ",intersectPoint.z)
        except ZeroDivisionError:
            print("WARNING - caught divide by zero error in getTwist")
            return 0
        
        #Put points on same Z plane
        lShoulder = XYZ([self.leftShoulder.x,self.leftShoulder.y,0])
        lHip = XYZ([self.leftHip.x,self.leftHip.y,0])
        
        dist_LShoulderIntersect = XYZ.getDistanceBetweenPoints(lShoulder,intersectPoint)
        dist_LHipIntersect = XYZ.getDistanceBetweenPoints(lHip,intersectPoint)
        dist_LShoulderLHip = XYZ.getDistanceBetweenPoints(lShoulder, lHip)
    
        a = dist_LShoulderIntersect
        b = dist_LHipIntersect
        c = dist_LShoulderLHip

        #Gets the Angle of C (T8 and UP)
        degrees = XYZ.getAngleOfTriangle(a,b,c)
            
        if (degrees > 90):
            degrees = 180 - degrees
                
        return degrees

 
    @staticmethod    
    # Map Shoulder Line Segment Origin to Hip Line Segment Origin
    def getTranslation(pt1, pt2):
        x = pt1.x - pt2.x
        y = pt1.y - pt2.y
        z = pt1.z - pt2.z
        translationVector = XYZ([x, y, z])
        return translationVector

 
    @staticmethod    
    def getYIntersect(x,y,m):
            return y-(m*x)
            
    @staticmethod    
    def getLineSlope(pt1,pt2):
        return (pt2.y - pt1.y) / (pt2.x - pt1.x)

    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    @staticmethod
    def getIntersectionOfTwoLines(m1,m2,c,d):
        x = (d-c) / (m1-m2)
        y = m1*x + c
        
        return XYZ([x,y,0])
        