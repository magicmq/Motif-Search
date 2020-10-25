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
# Class MotifLocateMaster
#
# Function: Locate a specific motif
#
#           This class defines help functions and
#           calls the motif locating algorithm
#
# ##########################################################

from MotifAbstract import MotifAbstract
from MotifLocate import MotifLocate


class MotifLocateMaster(MotifAbstract):
    motif = ""
    name = ""
    outName = ""
    appendVersion = False

    def printToFile(self, dat, outName):
        output = open(outName + ".txt", "w")

        output.write("---Motif Locations---\n")
        output.write("Motif: " + self.motif + "\n")

        for key in dat.keys():                     # Iterates through each clone the motif was found in
            output.write(key + "\n")
            temp = dat.get(key)                    # Grabs nucleotide locations of motif (indexes)
            seq = super().getSequences().get(key)  # Grabs clone nucleotide sequence
            endIndexes = []                        # Holds indexes of end motifs

            for x in range(len(seq)):              # Prints out sequence one nucleotide at a time
                if temp and (x + 1) == (temp[0] - super().getFPrimerSize()):
                    temp.pop(0)
                    output.write("(")
                    endIndexes.append((x + (len(self.motif) - 1)))
                output.write(seq[x : x+1])
                if endIndexes and x == endIndexes[0]:
                    output.write(")")
                    endIndexes.pop(0)
            output.write("\n")
        output.close()

    def appendToFile(self, dat, outName):
        output = open(outName + ".txt", "a")

        output.write("\nMotif: " + self.motif + "\n")

        for key in dat.keys():                     # Iterates through each clone the motif was found in
            output.write(key + "\n")
            temp = dat.get(key)                    # Grabs nucleotide locations of motif (indexes)
            seq = super().getSequences().get(key)  # Grabs clone nucleotide sequence
            endIndexes = []                        # Holds indexes of end motifs

            for x in range(len(seq)):              # Prints out sequence one nucleotide at a time
                if temp and (x + 1) == (temp[0] - super().getFPrimerSize()):
                    temp.pop(0)
                    output.write("(")
                    endIndexes.append((x + (len(self.motif) - 1)))
                output.write(seq[x: x + 1])
                if endIndexes and x == endIndexes[0]:
                    output.write(")")
                    endIndexes.pop(0)
            output.write("\n")
        output.close()

    def __init__(self, name, outName, motif):
        self.name = name
        self.outName = outName
        self.motif = motif

    def process(self):
        super().readFile(self.name)
        locate = MotifLocate(super().getSequences(), self.motif, super().getSeqSize(), super().getFPrimerSize())
        dat = locate.locateMotif()

        if(self.appendVersion):
            self.appendToFile(dat, self.outName)
        else:
            self.printToFile(dat, self.outName)

        print("\nProcess complete.\n")
