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
# Class MotifAbstract
#
# Function: Base class for search algorithm driver.
#           It reads and parses the input file
#
# ##########################################################

from abc import ABC
import re


class MotifAbstract(ABC):
    sequences = {}
    seqSize = 0
    fPrimerSize = 0

    def readFile(self, args):
        rFile = open(args, "r")
        rFileLines = rFile.readlines()
        rFileIt = iter(rFileLines)

        self.seqSize = int(re.sub("[^0-9]", "", rFileIt.__next__().split()[1]))

        # Skips junk lines
        for x in range(4):
            rFileIt.__next__()

        # Figures out the location of the random nucleotide sequence
        secondRead = ""
        lines = 0

        firstRead = rFileIt.__next__()
        firstN = firstRead.index("N")                   # Index of first N of the *unedited* sequence
        self.fPrimerSize = re.sub("[^A-Z]", "", firstRead).index("N")
        temp = rFileIt.__next__()
        while temp.__contains__("N"):
            secondRead = temp
            temp = rFileIt.__next__()
            lines += 1
        lastN = secondRead.rindex("N") + 1              # Index of last N of the *unedited* sequence

        # Adds sequences to the table; clone (key), sequence (value)
        while True:
            try:
                # Isolates clone number
                temp = rFileIt.__next__()
                clone = temp[temp.rindex("c") : temp.index("_")]

                # Skips junk lines
                for x in range(4):
                    rFileIt.__next__()

                # Isolates random nucleotide sequence
                firstRead = rFileIt.__next__()
                for x in range(lines):
                    secondRead = rFileIt.__next__()
                seq = re.sub("[^ACGT-]", "", (firstRead[firstN : ] + secondRead[0 : lastN]))

                # Adds data to the hashtable
                self.sequences[clone] = seq

                # Skips junk lines
                temp = rFileIt.__next__()
                while not temp.__contains__("//"):
                    temp = rFileIt.__next__()

            except StopIteration:
                break

    # Abstract methods
    def run(self):
        pass

    def printToFile(self, dat, outName):
        pass

    def appendToFile(self, dat, outName):
        pass

    # Get methods
    def getSequences(self):
        return self.sequences

    def getSeqSize(self):
        return self.seqSize

    def getFPrimerSize(self):
        return self.fPrimerSize
