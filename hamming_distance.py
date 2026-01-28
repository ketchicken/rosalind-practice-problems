"""
Problem

Given two strings s and t of equal length, the Hamming distance between s and t, 
denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s
 and t
 of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)
"""

def hamming_distance(s:str, t:str)->int:
    return sum(0 if s_n == t_n else 1 for s_n, t_n in zip(s, t))

file = "rosalind_hamm.txt"
with open(file) as f:
    s = f.readline()
    t = f.readline()
    print(hamming_distance(s, t))