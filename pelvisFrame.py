'''
Created on May 30, 2016

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

class pelvisFrame:

    def __init__(self, pelvisHeight):
        self.pelvisHeight  = pelvisHeight
    
    def getPelvisHeight(self):
        return self.pelvisHeight.z
    