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
# Class MotifLocate
#
# Function: Algorithm to locate a specific motif
#
# ##########################################################

class MotifLocate:
    # Constructor Variables
    sequences = {}              # Holds info of clones (keys) - sequences (values)
    keys = {}
    itKeys = iter(keys)
    motif = ""
    seqSize = 0                 # Following three variables all info regarding the motif that is being searched for
    primerSize = 0
    motSize = 0
    # Method Variables
    dat = {}                    # Return data; keys are motifs, values are lists of sequences the motif is found in
    refKey = ""                 # Following three variables all info regarding the tested motif
    refSeq = ""
    refMotif = ""

    # Constructor
    def __init__(self, seq, m, size, pSize):
        self.sequences = seq
        self.keys = seq.keys()
        self.itKeys = iter(self.keys)
        self.motif = m
        self.motSize = len(self.motif)
        self.seqSize = size
        self.primerSize = pSize

    # Locate Methods
    def locateMotif(self):
        while True:                     # Iterates through each clone
            try:
                refKey = self.itKeys.__next__()
                refSeq = self.sequences.get(refKey)
                n = 0                   # n = frame-shift
                locations = []

                #  Iterates through sequence of a clone, n shifts reading frame
                while (self.motSize + n) <= self.seqSize:
                    refMotif = refSeq[0+n : self.motSize+n]
                    if refMotif.__eq__(self.motif):
                        locations.append(self.primerSize + n + 1)
                    n += 1
                if locations:          # Checks to see if 'locations' has data inside
                    self.dat[refKey] = locations
            except StopIteration:
                break
        return self.dat

    #Get Methods
    def getResults(self):
        return self.dat
