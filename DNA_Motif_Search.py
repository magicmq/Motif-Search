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
# GUI Application Driver
#
# Function: Define search operation and parameters 
#           Call the search algorithm drivers
#
#           See Runner.py in the package for developer note
#
# ##########################################################

from MotifLocateMaster import MotifLocateMaster
from MotifSearchMaster import MotifSearchMaster

import os
import os.path
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

def getInputFile():
    global input_file
    running.set("")
    input_filetypes  = [('.gb files', '.gb'), ('All files', '.*')]
    input_file = filedialog.askopenfilename(parent=root,
                                            initialdir=os.getcwd(),
                                            title="Select an Input File",
                                            filetypes=input_filetypes)
    if os.path.exists(input_file):
        print("Input file " + input_file)
        inputF.set(input_file)
    else:  
        print("Input file " + input_file + " does not exist")
        exit()

def defineOutputFile():
    global output_file
    running.set("")
    output_filetypes = [('.txt files', '.txt')]
    output_file = filedialog.asksaveasfilename(parent=root,
                                               initialdir=os.getcwd(),
                                               title="Define Report File Name",
                                               filetypes=output_filetypes)
    if (".txt" in output_file):
        out = output_file.replace('.txt','')
        output_file = out

    print("Output file " + output_file + ".txt")
    outputF.set(output_file + ".txt")

# Disable search parameter entries based on Search or Locate operation
def disableEntry():
    val = int(my_var.get())
    if (val == 1):
        print("Search Motifs")
        size_entry.configure(state=tk.NORMAL)
        count_entry.configure(state=tk.NORMAL)
        motif_entry.configure(state=tk.DISABLED)
    else:
        print("Locate a Motif")
        size_entry.configure(state=tk.DISABLED)
        count_entry.configure(state=tk.DISABLED)
        motif_entry.configure(state=tk.NORMAL)
    running.set("")

def search():
    try:
        inputlength = len(input_file) 
    except:
        messagebox.showinfo('Error', 'Input file not defined!')
        return
        
    try:
        outputlength = len(output_file) 
    except:
        messagebox.showinfo('Error', 'Output file not defined!')
        return

    if os.path.exists(output_file + ".txt"):
        running.set("")
        msg = "Output file " + output_file + ".txt exists, overwrite it?"
        answer = messagebox.askquestion('Warning', msg)
        if answer == 'no':
            print("Please define a new output file")
            return
        else:
            print("Overwrite existing output file")

    val = int(my_var.get())
    if val == 1 :
        if int(minimum_motif_size.get()) < 3 :
            messagebox.showinfo('Error', '\"Minimum Motif Size\" must be larger than 2')
            print("Please enter a new value for Minimum Motif Size")
            return
        if int(minimum_motif_count.get()) < 2 :
            messagebox.showinfo('Error', '\"Minimum Occurrences\" of a motif must be larger than 1')
            print("Please enter a new value for Minimum Occurrences")
            return

        print("Running search ......")
        pro = MotifSearchMaster(input_file, output_file, minimum_motif_size.get(), minimum_motif_count.get())
        pro.process()

    else:
        if len( motif_to_search.get()) < 3 :
            messagebox.showinfo('Error', '\"Motif Pattern\" length must be larger than 2')
            print("Please enter a new Motif Pattern")
            return

        print("Running locate ......")
        pro = MotifLocateMaster(input_file, output_file, motif_to_search.get()) 
        pro.process()

    running.set("Completed")

# =========== Main Application =============

root = tk.Tk()
root.title("DNA Motif Search 1.0")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

minimum_motif_size  = StringVar()
minimum_motif_count = StringVar()
motif_to_search     = StringVar()

inputF  = StringVar()
outputF = StringVar() 

running = StringVar()

size_entry = ttk.Entry(mainframe, width=12, textvariable=minimum_motif_size)
size_entry.grid(column=2, row=5, sticky=(W, E))

count_entry = ttk.Entry(mainframe, width=12, textvariable=minimum_motif_count)
count_entry.grid(column=2, row=6, sticky=(W, E))

motif_entry = ttk.Entry(mainframe, width=12, textvariable=motif_to_search)
motif_entry.grid(column=2, row=7, sticky=(W, E))

my_var = StringVar()
ttk.Radiobutton(mainframe, text='Search All Motifs', variable=my_var, value=1, command=disableEntry).grid(column=2, row=1)
ttk.Radiobutton(mainframe, text='Locate One Motif', variable=my_var, value=2, command=disableEntry).grid(column=2, row=2)

ttk.Button(mainframe, text="Select Input File", command=getInputFile).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Define Report File", command=defineOutputFile).grid(column=2, row=8, sticky=(W, E))
ttk.Button(mainframe, text="Run", command=search).grid(column=2, row=10, sticky=W)

ttk.Label(mainframe, text="Select an Operation").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Selected Input File").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, text=" ---------------------- ").grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, textvariable=inputF).grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text="Minimum Motif Size").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="Minimum Occurrences").grid(column=1, row=6, sticky=E)
ttk.Label(mainframe, text="Motif Pattern").grid(column=1, row=7, sticky=E)
ttk.Label(mainframe, text="Selected Report File").grid(column=1, row=9, sticky=E)
ttk.Label(mainframe, text=" ---------------------- ").grid(column=2, row=9, sticky=(W, E))
ttk.Label(mainframe, textvariable=outputF).grid(column=3, row=9, sticky=W)
ttk.Label(mainframe, textvariable=running).grid(column=3, row=10, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()

# End
