############################################################
#                   Motif Search in DNA                
#                                                       
# This Python 3 application searches all potential sequence     
# motifs in a DNA or locate a specific motif in it.                 
#                                                      
# Author:      Sophie R. Liu                          
#              University of Texas at Austin           
#
# Last update: October 28, 2019                        
#
# Copyright (c) 2019  Sophie R. Liu
#
# This application is licensed under The MIT License.
# (See this application's dirver files for license text,
#  or https://opensource.org/licenses/MIT.)
#
# ##########################################################
#
# Class MotifSearchMaster 
#
# Function: Search the location of all motifs
#
#           This class defines help functions and
#           calls the motif search algorithm
#
# ##########################################################

from MotifAbstract import MotifAbstract
from MotifSearch import MotifSearch


class MotifSearchMaster(MotifAbstract):
    motSize = 0
    motIncident = 0
    name = ""
    outName = ""
    appendVersion = False

    def form(self, list):
        size = len(list)
        ret = ""
        for x in range(size - 1):
            ret += list[x] + ", "
        ret += list[size - 1]
        return ret

    def printToFile(self, dat, outName):
        output = open(outName + ".txt", "w")

        output.write("---Found Motifs---\n")
        output.write("Minimum motif size: " + str(self.motSize) + "\t\tMinimum motif incident number: " +
                     str(self.motIncident))
        output.write("\nUnique motifs found:  " + str(len(dat)) + "\n")

        for key in sorted(dat.keys()):
            output.write(key + ": \n")
            output.write(self.form(dat.get(key)) + "\n\n")

        output.close()

    def appendToFile(self, dat, outName):
        output = open(outName + ".txt", "a")

        output.write("-----")
        output.write("\nMinimum motif size: " + str(self.motSize) + "\t\tMinimum motif incident number: " +
                     str(self.motIncident))
        output.write("\nUnique motifs found:  " + str(len(dat)) + "\n")

        for key in sorted(dat.keys()):
            output.write(key + ": \n")
            output.write(self.form(dat.get(key)) + "\n\n")

        output.close()

    def __init__(self, name, outputName, motSize, motIncident):
        self.name = name
        self.outName = outputName
        self.motSize = int(motSize)
        self.motIncident = int(motIncident)

    def process(self):
        super().readFile(self.name)
        search = MotifSearch(super().getSequences(), super().getSeqSize(), super().getFPrimerSize(), 
                             self.motSize, self.motIncident)
        dat = search.searchMotif()

        if (self.appendVersion):
            self.appendToFile(dat, self.outName)
        else:
            self.printToFile(dat, self.outName)

        print("\nProcess complete.\n")
