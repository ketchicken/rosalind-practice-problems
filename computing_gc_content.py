"""
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""
#import re

class FASTAParser:
    def __init__(self, fasta_file):
        self.sequences = {}
        with open(fasta_file) as f:
            data = f.read().split('>')
            data.pop(0)
            
            for run in data:
                key, sequence = self.clean_run(run)
                self.sequences[key] = sequence
    
    def clean_run(self, rough_data:str):
        key = rough_data.split('\n')[0]
        sequence = rough_data[len(key):].replace('\n', '')
        return key, sequence
        
    def gc_content(self, key):
        sequence = self.sequences[key]
        g_count = sequence.count("G")
        c_count = sequence.count("C")
        
        return (g_count + c_count) / len(sequence) if len(sequence) else 0

    def max_gc_content(self)->str:
        max_gc = 0
        max_id = ""
        for iD in self.sequences.keys():
            gc_content = self.gc_content(iD)
            if max_gc < gc_content:
                max_gc = gc_content
                max_id = iD
        max_gc = round(max_gc * 100, 3)
        return f"{max_id}\n{max_gc}"

def __main__():
    #fasta_file = input("Enter path to FASTA file: ")
    gc_computer = FASTAParser("rosalind_gc.txt")
    print(gc_computer.max_gc_content())

__main__()