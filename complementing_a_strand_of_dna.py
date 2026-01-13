"""
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
 is the string sc
 formed by reversing the symbols of s
, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s
 of length at most 1000 bp.

Return: The reverse complement sc
 of s
.

Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT
"""

def compliment_dna(dnaString: str)->str:
    ''' Take a string of DNA and return the compliment of it '''
    complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
    complement_string = ""

    for nt in dnaString:
        complement_string = complement.get(nt,"") + complement_string
    
    return complement_string

to_complement = input("Enter DNA string")

print(compliment_dna(to_complement))