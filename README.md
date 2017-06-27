# Motion-Tracking-Data-Parser
# Source: Builds under Python v2.7

Extracts key metrics from motion tracking data (in MVNX / XML format).  Extract data can be used to determine if lifting and transfer movements risk injury.  Software is based on research paper presented at ACM Digital Health Conference (DigH) 2017.

## Input Data
By default data is input in the same source directory as source code. Four sample data files are provided.  Code runs a single file (0_Bed_to_ShowerChair_M.mvnx) by default, but you can add the others by editting main.py.   If you input MVNX or XML file follows different formatting rules, you will need to edit MotionCaptureExecutor.py and edit the parsing rules.

## Results
By default results are placed in the results.csv

## Details
Please read the following research paper for details.  

## License

Users are encouraged to use, modify and extend this work under the GNU GPLv3 license.

Please cite the following paper to provide credit to this work:

Jonathan Muckell, Yuchi Young, and Mitch Leventhal. 2017. 
A Wearable Motion Tracking System to Reduce Direct Care Worker Injuries: An Exploratory Study. 
In Proceedings of DH ’17, London, United Kingdom, July 02-05, 2017, 5 pages.
DOI: hp://dx.doi.org/10.1145/3079452.3079493
