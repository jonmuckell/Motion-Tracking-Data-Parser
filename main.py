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

#run("0_Bed_to_ShowerChair_M.mvnx",  [0, 1480, 1600, 2000, 2200, 2600])
run("0_Bed_to_ShowerChair_N.mvnx", [0, 1150, 3041, 3450, 4100, 7500] )

'''
run("0_ShowerChair_to_WheelChair_M.mvnx", [0, 2000, 2550, 2700, 2850, 5000] )
run("0_ShowerChair_to_WheelChair_N.mvnx", [0, 1550, 1820, 2400, 2800,  7000 ])

run("1_Bed_to_showerChair_M.mvnx", [0, 900, 1050, 1200, 1380, 1500])
run("1_Bed_to_showerChair_N.mvnx", [0, 1050, 1320, 1400, 1650, 1800 ])
run("1_ShowerChair_to_WheelChair_M.mvnx",[0, 650, 800, 1450, 1700, 2000])
run("1_ShowerChair_to_WheelChair_N.mvnx", [0, 630, 920, 1000, 1400, 1550 ])

run("2_bed_to_ShowerChair_M.mvnx",[0, 1800, 2200, 2325, 2800, 2900 ])
run("2_Bed_to_ShowerChair_N.mvnx",[0, 1550, 1790, 1950, 2350, 2500] )
run("2_showerChair_to_wheelChair_M.mvnx", [0, 800, 1070, 1300, 1700, 2500 ])
run("2_ShowerChair_to_WheelChair_N.mvnx", [2700, 4100, 4370, 4500, 5400, 5500])

run("3_bed_to_chair_M.mvnx", [0, 950, 1100, 1300, 1700, 1750])

run("3_bed_to_showerChair_N.mvnx", [0, 1450, 2050, 2400, 2600, 3000])  

run("3_WheelChair_to_Chair_M.mvnx", [0, 250, 550, 1150, 1470, 1500])

run("4_Bed_to_shower_N.mvnx", [2000, 2600, 2900, 3000, 3500, 3750] )
run("4_Bed_to_showerChair_M.mvnx", [0, 2700, 3000, 3100, 3300, 3500])

run("5_Bed_to_ShowerChair_M.mvnx", [0, 400, 600, 650, 1050, 1100])
run("5_bed_to_ShowerChair_N.mvnx", [6300, 7600, 8000, 8300, 8500, 8650])
run("5_ShowerChair_to_WheelChair_M.mvnx",[0, 450, 700, 800, 950, 1100])
run("5_ShowerChair_to_WheelChair_N.mvnx", [0, 2400, 2700, 3850, 4150, 4350])

run("6_Bed_to_ShowerChair_M.mvnx", [0, 1050, 1230, 1320, 1450, 1600])
run("6_bed_to_showerChair_N.mvnx", [0, 3000, 3470, 3500, 3750, 3900])
run("6_ShowerChair_to_WheelChair_M.mvnx", [0, 320, 450, 470, 735, 1200])
run("6_ShowerChair_to_WheelChair_N.mvnx", [0, 1400, 1480, 1550, 1900, 3300])

run("7_Bed_to_showerchair_M.mvnx", [0, 1130, 1265, 1350, 1560, 1600])
run("7_bed_to_showerChair_N.mvnx",[0, 1400, 1500, 1700, 2000, 2150])
run("7_showerChair_to_wheelchair_M.mvnx", [0, 400, 520, 710, 1000, 2100])
run("7_showerChair_to_Wheelchair_N.mvnx", [0, 1000, 1125, 1300, 1560, 1800])
'''
#------------------------------------
resultsFileHandler.close()
print("CODE FINISHED!")
