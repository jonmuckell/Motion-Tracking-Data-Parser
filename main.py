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
from motionCaptureExecutor import motionCaptureExecutor

# ---- CONFIGS ----
standardOut = True
writeToFile = False
resultsFileHander = ""

def run(xmlfile, segmentIDXs):
    mce = motionCaptureExecutor()
   
    mce.setXMLFile(xmlfile)

    mce.setStartIDX(segmentIDXs[0])
    mce.setLiftIDX(segmentIDXs[1])
    mce.setTransferIDX(segmentIDXs[2])
    mce.setDropIDX(segmentIDXs[3])
    mce.setSeatCheckIDX(segmentIDXs[4])
    mce.setEndIDX(segmentIDXs[5])

    mce.buildMotionCapture()
    if (standardOut):
        mce.runBackBendMotionCapture()
        mce.runPelvisHeightMotionCapture()
        mce.runSupportBaseMotionCapture()
        mce.runTwistMotionCapture()
    
    if(writeToFile):
        mce.writeHeadersToFile(resultsFileHandler)
        mce.writeToFile(resultsFileHandler)
   
    print("------------ Finished -----------")




print("CODE STARTED!")

resultsFileHandler = open('results.csv', 'a')
    

# start, lift, transfer, drop, post, end
#------------------------------------

run("0_Bed_to_ShowerChair_M.mvnx",  [0, 1480, 1600, 2000, 2200, 2600])
#run("0_Bed_to_ShowerChair_N.mvnx", [0, 1150, 3041, 3450, 4100, 7500] )
#run("0_ShowerChair_to_WheelChair_M.mvnx", [0, 2000, 2550, 2700, 2850, 5000] )
#run("0_ShowerChair_to_WheelChair_N.mvnx", [0, 1550, 1820, 2400, 2800,  7000 ])


#------------------------------------
resultsFileHandler.close()
print("CODE FINISHED!")
