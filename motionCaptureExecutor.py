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

import xml.etree.ElementTree
from fileParser import fileParser
from motionCapture import motionCapture
from XYZ import XYZ
from twistFrame import twistFrame


class motionCaptureExecutor:
    
    def __init__(self):
        self.xmlFile = ""
        self.mc = motionCapture()
        self.startIDX = -1
        self.liftStartIDX = -1;
        self.transferStartIDX = -1
        self.dropStartIDX = -1
        self.seatCheckIDX = -1
        self.endIDX = -1
        
# ---------------------------------------------------------------
# ---------------------------------------------------------------
    def setXMLFile(self, xmlFile):
        print("XML File: ", xmlFile)
        self.xmlFile = xmlFile
   
    def setStartIDX(self, idx):
        self.startIDX = idx
    def setLiftIDX(self, idx):
        self.liftStartIDX = idx
    def setTransferIDX(self, idx):
        self.transferStartIDX = idx    
    def setDropIDX(self, idx):
        self.dropStartIDX = idx 
    def setSeatCheckIDX(self, idx):
        self.seatCheckIDX = idx            
    def setEndIDX(self, idx):
        self.endIDX = idx 

# ---------------------------------------------------------------
# ---------------------------------------------------------------

    def buildMotionCapture(self):
        L5 = fileParser.getTagElements(self.xmlFile, 'position',2)
        T8 = fileParser.getTagElements(self.xmlFile, 'position',5)
        self.mc.setSpineFrames(L5,T8)
        pelvis  = fileParser.getTagElements(self.xmlFile, 'position',1)
        self.mc.setPelvisFrames(pelvis)
        leftFoot  = fileParser.getTagElements(self.xmlFile, 'position',22)
        rightFoot  = fileParser.getTagElements(self.xmlFile, 'position',18)
        self.mc.setFeetFrames(leftFoot,rightFoot)
        leftShoulder  = fileParser.getTagElements(self.xmlFile, 'position',12)
        rightShoulder  = fileParser.getTagElements(self.xmlFile, 'position',8)
        leftUpperLeg  = fileParser.getTagElements(self.xmlFile, 'position',20)
        rightUpperLeg  = fileParser.getTagElements(self.xmlFile, 'position',16)
        self.mc.setTwistFrames(leftShoulder, rightShoulder, leftUpperLeg, rightUpperLeg)
# ---------------------------------------------------------------
# ---------------------------------------------------------------

    def runBackBendMotionCapture(self):
        print("---------Back/Spine Max Angle---------")
        print("Overall: ", self.mc.getOverall_MaxBend())
        print("prep: ", self.getPrep_MaxBend())
        print("lift: ", self.getLift_MaxBend())
        print("transfer: ", self.getTransfer_MaxBend())
        print("drop: ", self.getDrop_MaxBend())
        print("post: ", self.getPost_MaxBend())

    def runPelvisHeightMotionCapture(self):
        print("---------Pelvis Min Height Motion Capture---------")
        print("Overall: ", self.mc.getOverall_MinPelvisHeight())
        print("prep: ", self.getPrep_MinPelvisHeight())
        print("lift: ", self.getLift_MinPelvisHeight())
        print("transfer: ", self.getTransfer_MinPelvisHeight())
        print("drop: ", self.getDrop_MinPelvisHeight())        
        print("post: ", self.getPost_MinPelvisHeight())

    def runSupportBaseMotionCapture(self):
        print("---------Support Base Max - Motion Capture---------")
        print("Overall: ", self.mc.getOverall_MaxSupportBase())
        print("prep: ", self.getPrep_MaxSupportBase())
        print("lift: ", self.getLift_MaxSupportBase())
        print("transfer: ", self.getTransfer_MaxSupportBase())
        print("drop: ", self.getDrop_MaxSupportBase())
        print("post: ", self.getPost_MaxSupportBase())
        
    
    def runTwistMotionCapture(self):
        print("---------Twist Max - Motion Capture---------")
        print("Overall: ", self.mc.getOverall_MaxTwist())
        print("prep: ", self.getPrep_MaxTwist())
        print("lift: ", self.getLift_MaxTwist())
        print("transfer: ", self.getTransfer_MaxTwist())
        print("drop: ", self.getDrop_MaxTwist())
        print("post: ", self.getPost_MaxTwist())

        
    def runOverallStats(self):
        print("Overall - Max Bend: ", self.mc.getOverall_MaxBend())
        print("Overall - MinPelvis: ", self.mc.getOverall_MinPelvisHeight())
        print("Overall - Max SupportBase: ", self.mc.getOverall_MaxSupportBase())
        print("Overall - Max Twist: ", self.mc.getOverall_MaxTwist())
               

# ----------------------------------------------
# ----------------------------------------------

    def writeHeadersToFile(self, fileHandle):
        fileHandle.write("File,")
        fileHandle.write("Overall_MaxBend,Prep_MaxBend , Lift_MaxBend , Transfer_MaxBend , Drop_MaxBend , Post_MaxBend ,")
        fileHandle.write("Overall_MaxTwist, Prep_MaxTwist , Lift_MaxTwist , Transfer_MaxTwist , Drop_MaxTwist , Post_MaxTwist ,")
        fileHandle.write("Overall_MinPelvisHeight, Prep_MinPelvisHeight , Lift_MinPelvisHeight , Transfer_MinPelvisHeight , Drop_MinPelvisHeight , Post_MinPelvisHeight ,")
        fileHandle.write("Overall_MaxSupportBase, Prep_MaxSupportBase , Lift_MaxSupportBase , Transfer_MaxSupportBase , Drop_MaxSupportBase , Post_MaxSupportBase ,")
        fileHandle.write("\n")
        
 
    def writeToFile(self, fileHandle):
        line = self.xmlFile + ","
        line = line + str(self.mc.getOverall_MaxBend())+","+str(self.getPrep_MaxBend())+","+str(self.getLift_MaxBend())+","+str(self.getTransfer_MaxBend())+","+str(self.getDrop_MaxBend())+","+str(self.getPost_MaxBend())+","
        line = line + str(self.mc.getOverall_MaxTwist())+","+str(self.getPrep_MaxTwist())+","+str(self.getLift_MaxTwist())+","+str(self.getTransfer_MaxTwist())+","+str(self.getDrop_MaxTwist())+","+str(self.getPost_MaxTwist())+","
        line = line + str(self.mc.getOverall_MinPelvisHeight())+","+str(self.getPrep_MinPelvisHeight())+","+str(self.getLift_MinPelvisHeight())+","+str(self.getTransfer_MinPelvisHeight())+","+str(self.getDrop_MinPelvisHeight())+","+str(self.getPost_MinPelvisHeight())+","
        line = line + str(self.mc.getOverall_MaxSupportBase())+","+str(self.getPrep_MaxSupportBase())+","+str(self.getLift_MaxSupportBase())+","+str(self.getTransfer_MaxSupportBase())+","+str(self.getDrop_MaxSupportBase())+","+str(self.getPost_MaxSupportBase())+","
        line = line + "\n"
        fileHandle.write(line)

# ----------------------------------------------
# ----------------------------------------------

    def getPrep_MinPelvisHeight(self):
        return self.mc.getMinPelvisHeight(self.startIDX, self.liftStartIDX)

    def getLift_MinPelvisHeight(self):
        return self.mc.getMinPelvisHeight(self.liftStartIDX,self.transferStartIDX)
        
    def getTransfer_MinPelvisHeight(self):
        return self.mc.getMinPelvisHeight(self.transferStartIDX, self.dropStartIDX)
 
    def getDrop_MinPelvisHeight(self):
        return self.mc.getMinPelvisHeight(self.dropStartIDX, self.seatCheckIDX)

    def getPost_MinPelvisHeight(self):
        return self.mc.getMinPelvisHeight(self.seatCheckIDX,self.endIDX)

# ---------------------------------------------------------------
# ---------------------------------------------------------------

    def getPrep_MaxBend(self):
        return self.mc.getMaxBend(self.startIDX, self.liftStartIDX)

    def getLift_MaxBend(self):
        return self.mc.getMaxBend(self.liftStartIDX,self.transferStartIDX)
        
    def getTransfer_MaxBend(self):
        return self.mc.getMaxBend(self.transferStartIDX, self.dropStartIDX)
 
    def getDrop_MaxBend(self):
        return self.mc.getMaxBend(self.dropStartIDX, self.seatCheckIDX)

    def getPost_MaxBend(self):
        return self.mc.getMaxBend(self.seatCheckIDX,self.endIDX)

# ---------------------------------------------------------------
# ---------------------------------------------------------------

    def getPrep_MaxSupportBase(self):
        return self.mc.getMaxSupportBase(self.startIDX, self.liftStartIDX)

    def getLift_MaxSupportBase(self):
        return self.mc.getMaxSupportBase(self.liftStartIDX,self.transferStartIDX)
        
    def getTransfer_MaxSupportBase(self):
        return self.mc.getMaxSupportBase(self.transferStartIDX, self.dropStartIDX)
 
    def getDrop_MaxSupportBase(self):
        return self.mc.getMaxSupportBase(self.dropStartIDX, self.seatCheckIDX)

    def getPost_MaxSupportBase(self):
        return self.mc.getMaxSupportBase(self.seatCheckIDX,self.endIDX)

# ---------------------------------------------------------------
# ---------------------------------------------------------------

    def getPrep_MaxTwist(self):
        return self.mc.getMaxTwist(self.startIDX, self.liftStartIDX)

    def getLift_MaxTwist(self):
        return self.mc.getMaxTwist(self.liftStartIDX,self.transferStartIDX)
        
    def getTransfer_MaxTwist(self):
        return self.mc.getMaxTwist(self.transferStartIDX, self.dropStartIDX)
 
    def getDrop_MaxTwist(self):
        return self.mc.getMaxTwist(self.dropStartIDX, self.seatCheckIDX)

    def getPost_MaxTwist(self):
        return self.mc.getMaxTwist(self.seatCheckIDX,self.endIDX)
