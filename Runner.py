############################################################
#                   Motif Search in DNA                
#                                                       
# This Python 3 application searches all potential sequence     
# motifs in a DNA or locate a specific motif in it.                 
#                                                      
# Author:      Sophie R. Liu                          
#              University of Texas at Austin           
#              sliu678876@gmail.com
#
# Last update: October 28, 2019                        
#
############################################################ 
#
# This application is licensed under The MIT License.
# (See also https://opensource.org/licenses/MIT for details.)
#
# Copyright (c) 2019  Sophie R. Liu 
#
# Permission is hereby granted, free of charge, to any person 
# obtaining a copy of this software and associated documentation 
# files (the "Software"), to deal in the Software without 
# restriction, including without limitation the rights to use, 
# copy, modify, merge, publish, distribute, sublicense, and/or 
# sell copies of the Software, and to permit persons to whom 
# the Software is furnished to do so, subject to the following 
# conditions:
#
# The above copyright notice and this permission notice shall 
# be included in all copies or substantial portions of the 
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY 
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR 
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# ##########################################################
#
# Command Line Application Driver
#
# Function: Define search operation and parameters 
#           Call the search algorithm drivers
#
# ##########################################################

#  Developer Note:
#
#  This application was developed to help my labmates and myself 
#  identify motifs more efficiently than we used to do.
#
#  It has this command line driver and a GUI dirver.  
#  The command line driver is easier for debugging.
#  The GUI driver is more user friendly.
#
#  I've done my best to make my code as readable as possible, 
#  with additional comments to help explain variable and method  
#  functions to help you (and myself) navigate.
#
#  Just to preface, I am no CS major, nor a CS minor. I have  
#  moderate experience in Java, and I am novice to Python -- 
#  this program itself was initially constructed in Java before
#  it was moved over to Python for easier deployment with some
#  performance sacrifice.
#
#  There are definitely oddities or artifiacts in this code.   
#  Let's get one point across: this program is far from perfect.  
#  I doubt it is constructed in the most efficient way possible, 
#  and there's likely going to be times where my coding decisions 
#  seem to be questionable.  But that's why this code is open 
#  source - so it can be constantly updated fixed, and improved
#  to make this the best it can possibly be. Don't be afraid of
#  making some changes here or here, or completely refactoring 
#  what I have if you can construct something more efficient 
#  and clean. I appreciate yoiur suggestiions and corrections.


from MotifLocateMaster import MotifLocateMaster
from MotifSearchMaster import MotifSearchMaster


# Determines if response is a legal response
def programExecuteType(args):
    args = args.casefold()
    switcher = {
        "search": True,
        "locate": True
    }
    return switcher.get(args, False)


# Defines variables, asks for which program to execute
answer = ""
contin = True

while contin:
    responseF = False
    while not responseF:
        answer = input("Search for motifs or locate a motif? ")
        responseF = programExecuteType(answer)
        if not responseF:
            print("\n***Answer not valid, please re-enter your response.")

    # Runs the appropriate code
    answer = answer.casefold()

    if answer == "locate":
        print("Locate function executed")
        print("\n---------------------------------------------------------------------------------------------------\n")
        name = input("Input the name of the data file: ")
        motif = input("Motif: ").upper()
        outName = input("Name of output file? (Do not include file extension, automatically returns '.txt') ")

        ex = MotifLocateMaster(name, outName, motif)
        ex.process()

    else:
        print("Search function executed")
        print("\n---------------------------------------------------------------------------------------------------\n")
        name = input("Input the name of the data file: ")
        motSize = input("Minimum motif size? ")
        motIncident = input("Minimum number of motif incidents? ")
        outName = input("Name of output file? (Do not include file extension, automatically returns '.txt') ")

        # We cannot support append which will give wrong results
        #addOn = input("Append the results to an existing file? (Y/N) ")
        #appendVersion = addOn.casefold().__eq__("y")

        ex = MotifSearchMaster(name, outName, motSize, motIncident)
        ex.process()

    contAnswer = input("\n\nWould you like to run another function? (Y/N) ")
    contin = contAnswer.casefold().__eq__("y")
