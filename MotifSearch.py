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
# Class MotifSearch
#
# Function: Algorithm to search all motifs
#
# ##########################################################

class MotifSearch:
    # Constructor Variables
    sequences = {}                  # Holds info of clones (keys) - sequences (values)
    keys = {}
    itKeys = iter(keys)
    motif = ""
    seqSize = 0                     # Following three variables all info regarding the motif that is being searched for
    primerSize = 0
    motSize = 0
    motIncident = 0
    # Method Variables
    dat = {}                        # Return data; keys are motifs, values are lists of sequences the motif is found in
    refKey = ""                     # Following three variables all info regarding the tested motif
    refSeq = ""
    refMotif = ""
    itSearch = iter(keys)
    compKey = ""                    # Following three variables all info regarding compared sequences
    compSeq = ""
    comMotif = ""

    # Constructor
    def __init__(self, seq, size, pSize, mSize, mIncident):
        self.sequences = seq
        self.keys = seq.keys()
        self.itKeys = iter(self.keys)
        self.seqSize = size
        self.primerSize = pSize
        self.motSize = mSize
        self.motIncident = mIncident

    # Helper Methods
    def refine(self):
        motifs = self.dat.keys()
        redundant = set()

        # Checks for redundancies where smaller motifs are part of larger ones and both have same # of incidents
        for test in motifs:
            for check in motifs:
                # 'test' is the smaller motif, 'check' the larger
                if not check.__eq__(test) and test in check and len(self.dat[check]) == len(self.dat[test]):
                    redundant.add(test)

        # Actually removes the redundancies
        for remove in redundant:
            self.dat.pop(remove)

    # Search Methods
    # Once potential unique motif found, searches for other copies
    def helpSearch(self, n, x):
        # n = frame-shift of reference motif; x = change to reading frame compared to motSize / deviation from motSize
        # Adds original key motif was found in
        foundMotifs = [self.refKey + " - " + str(self.primerSize + n + 1)]

        itSearch = iter(self.keys)
        while True:                     # Iterates through each clone for comparison
            try:
                self.compKey = itSearch.__next__()
                self.compSeq = self.sequences.get(self.compKey)
                m = 0                   # m = frame-shift of compared sequences; this statement resets reading frame

                # Iterates through each possible motif of size 'motSize + x,' making sure both compared sequences are
                # different
                while (self.motSize + x) + m <= self.seqSize:
                    self.compMotif = self.compSeq[0+m : (self.motSize+x)+m]

                    # Checks if compMotif ad refMotif are the same; if so, adds compKey to list of foundMotifs
                    if "-" not in self.compMotif and (not self.compSeq.__eq__(self.refSeq) or not m == n) and \
                            self.compMotif.__eq__(self.refMotif):
                        foundMotifs.append(self.compKey + " - " + str(self.primerSize + m + 1))
                    m += 1

            except StopIteration:
                break

        # Once done iterating, adds foundMotifs to dat if the motif was found at least 'motIncident' number of times
        if len(foundMotifs) >= self.motIncident:
            self.dat[self.refMotif] = foundMotifs

    # Searches for potentially unique motifs; once candidate found, delegates work to 'helpSearch'
    def searchMotif(self):
        self.dat = {}
        while True:
            try:
                self.refKey = self.itKeys.__next__()
                self.refSeq = self.sequences.get(self.refKey)
                n = 0                   # n = frame-shift
                x = 0                   # x = reading frame size (deviation from motSize)

                while (self.motSize + x) <= self.seqSize:
                    while (self.motSize + x) + n <= self.seqSize:
                        self.refMotif = self.refSeq[0+n : (self.motSize+x)+n]
                        if "-" not in self.refMotif and self.refMotif not in self.dat:
                            self.helpSearch(n, x)
                        n += 1
                    n = 0                   # Resets the reading frame frame-shift
                    x += 1                  # Increases the size of the reading frame
            except StopIteration:
                break

        # Refines search results to remove redundancies
        self.refine()

        return self.dat

    # Get Methods
    def getResults(self):
        return self.dat
