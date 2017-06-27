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


from XYZ import XYZ
import math

class spineFrame:

    def __init__(self, L5, T8):
        self.L5 = L5
        self.T8 = T8
    
    
    # Number of Sensor Readings
    def getNumberOfSensorReadings(self):
        if (len(self.L5) != len(self.T8)):
            print("ERROR - Number of sample readings doesn't match!")
        return len(self.L5)


    # Solve for back angle
    # Equation explained at https://www.mathsisfun.com/algebra/trig-cosine-law.html
    def getBackBendAngle(self):        
        upright = self.getPerfectUprightPt()
        dist_L5T8 = XYZ.getDistanceBetweenPoints(self.L5,self.T8)
        dist_L5Up = XYZ.getDistanceBetweenPoints(self.L5,upright)
        dist_T8Up = XYZ.getDistanceBetweenPoints(self.T8,upright)
        
        
        a = dist_L5T8
        b = dist_L5Up
        c = dist_T8Up

        #Gets the Angle of C (T8 and UP)
        degrees = XYZ.getAngleOfTriangle(a,b,c)
        return degrees
        
        
    def getPerfectUprightPt(self):
        return XYZ([self.L5.x,self.L5.y,10])
    
    
    