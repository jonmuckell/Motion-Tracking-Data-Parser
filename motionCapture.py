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
from spineFrame import spineFrame
from twistFrame import twistFrame
from pelvisFrame import pelvisFrame
from feetFrame import feetFrame

class motionCapture:

    def __init__(self):
        self = self
        self.spineFrames = []
        self.twistFrames = []
        self.pelvisFrames = []
        self.feetFrames = []    
                   
# ---------------------------------------------------------------
# ---------------------------------------------------------------
    
    def setSpineFrames(self, L5list, T8list):
        if (len(L5list) != len(T8list)):
            print("ERROR - NOT READING IN THE SAME NUMBER OF SENSOR READINGS FOR L5 and T8!!")     
        for i in range(0,len(L5list)):
            L5reading = XYZ(L5list[i])
            T8reading = XYZ(T8list[i])
            sframe = spineFrame(L5reading, T8reading)    
            self.spineFrames.append(sframe)

        
    def setTwistFrames(self, leftShoulderlist, rightShoulderlist, leftHiplist,rightHiplist):
        if (len(leftShoulderlist) != len(rightShoulderlist) != len(leftHiplist) != len(rightHiplist)):
            print("ERROR - NOT READING IN THE SAME NUMBER OF SENSOR READINGS FOR shoulders and hips!!")
        for i in range(0,len(leftShoulderlist)):
            leftShoulderReading = XYZ(leftShoulderlist[i])
            rightShoulderReading = XYZ(rightShoulderlist[i])
            leftHipReading = XYZ(leftHiplist[i])
            rightHipReading = XYZ(rightHiplist[i])
            tFrame = twistFrame(leftShoulderReading,rightShoulderReading,leftHipReading,rightHipReading)          
            self.twistFrames.append(tFrame)

        
    def setPelvisFrames(self, pelvisList):
        for i in range(0,len(pelvisList)):
            pelvisReading = XYZ(pelvisList[i])
            pframe = pelvisFrame(pelvisReading)    
            self.pelvisFrames.append(pframe)

        
    def setFeetFrames(self, leftFootList, rightFootList):
        if (len(leftFootList) != len(rightFootList)):
            print("ERROR - NOT READING IN THE SAME NUMBER OF SENSOR READINGS FOR feet!!")
        for i in range(0,len(leftFootList)):
            leftFootReading = XYZ(leftFootList[i])
            rightFootReading = XYZ(rightFootList[i])
            fFrame = feetFrame(leftFootReading,rightFootReading)
            self.feetFrames.append(fFrame)

# ---------------------------------------------------------------
# ---------------------------------------------------------------

    def getOverall_MaxBend(self):
        return self.getMaxBend(0, len(self.spineFrames))
    
    def getMaxBend(self, startIDX, endIDX):
        if(startIDX is -1 or endIDX is -1):
            print("Error - getMaxBend, indexes not set!")
        maxBend = -999999
        for i in range(startIDX,endIDX):
            sFrame = self.spineFrames[i]
            bend = sFrame.getBackBendAngle()
            if (bend > maxBend):
                maxBend = bend
        return maxBend

# ---------------------------------------------------------------
# ---------------------------------------------------------------

    def getOverall_MaxTwist(self):
        return self.getMaxTwist(0, len(self.twistFrames))
        
    def getMaxTwist(self,startIDX, endIDX):
        maxTwist = -999999
        maxTwistIndex = -999999
        for i in range(startIDX, endIDX):
            tFrame = self.twistFrames[i]
            twist = tFrame.getTwist()
#            print("twist=",round(twist,2))
            if (twist > maxTwist):
                maxTwist = twist
                maxTwistIndex = i
        
        #print("MAX Twist INDEX: ",maxTwistIndex)
        return maxTwist

# ---------------------------------------------------------------
# ---------------------------------------------------------------

    def getOverall_MinPelvisHeight(self):
        return self.getMinPelvisHeight(0, len(self.spineFrames))
    

    def getMinPelvisHeight(self,startIDX, endIDX):
        if(startIDX is -1 or endIDX is -1):
            print("Error - getMinPelvisHeight, indexes not set!")
        minHeight = 999999;
        for i in range(startIDX, endIDX):
            pFrame = self.pelvisFrames[i]
            height = pFrame.getPelvisHeight()
            #print("height=",round(height,2))
            if (height < minHeight):
                minHeight = height
        #print("Min Height: ",minHeight)
        return minHeight    

# ---------------------------------------------------------------
# ---------------------------------------------------------------

    def getOverall_MaxSupportBase(self):
        return self.getMaxSupportBase(0, len(self.spineFrames))
    
    def getMaxSupportBase(self, startIDX, endIDX):
        if(startIDX is -1 or endIDX is -1):
            print("Error - getMinPelvisHeight, indexes not set!")
        maxDistance = -999999;
        for i in range(startIDX, endIDX):
            fFrame = self.feetFrames[i]
            dist  = fFrame.getDistanceBetweenFeet()
            #print("dist =",round(dist,2))
            if (dist > maxDistance):
                maxDistance = dist
        #print("Max Distance: ",maxDistance)
        return maxDistance

# ---------------------------------------------------------------
# ---------------------------------------------------------------


    def getAveragePelvisHeight(self):
        sumHeight = 0;
        for i in range(0,len(self.pelvisFrames)):
            pFrame = self.pelvisFrames[i]
            height = pFrame.getPelvisHeight()
            #print("height=",height)
            sumHeight = sumHeight + height
        avgHeight = sumHeight / len(self.pelvisFrames)
        print("Average Height: ",avgHeight)
        return avgHeight


    def getAverageSupportBase(self):
        sumDistance = 0;
        for i in range(0,len(self.feetFrames)):
            fFrame = self.feetFrames[i]
            dist  = fFrame.getDistanceBetweenFeet()
            #print("dist =",dist)
            sumDistance = sumDistance + dist
        avgDistance = sumDistance / len(self.feetFrames)
        print("Average Distance: ",avgDistance)
        return avgDistance
