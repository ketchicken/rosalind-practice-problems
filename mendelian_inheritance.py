"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). 
Assume that any two organisms can mate.
"""
import math

def p_dominant(k:int, m:int, n:int)->float:
    ''' 
    Return a float representing the probability of an offspring between any pair with a dominant allele
    
    :param k: number of organisms that are homozygous dominant
    :param m: number of organisms that are heterozygous
    :param n: number of organisms that are homozygous recessive
    '''

    total_population = k + m + n
    possible_duos = math.comb(total_population, 2)

    k_k_duos = math.comb(k, 2)
    k_m_duos = k*m 
    k_n_duos = k*n
    m_m_duos = math.comb(m, 2)
    m_n_duos = m*n
    n_n_duos = math.comb(n, 2)

    p_k_k = k_k_duos / possible_duos
    p_k_m = k_m_duos / possible_duos
    p_k_n = k_n_duos / possible_duos
    p_m_m = m_m_duos / possible_duos
    p_m_n = m_n_duos / possible_duos
    p_n_n = n_n_duos / possible_duos

    # P(X | k and k) = 1
    # P(X | k and m) = 1
    # P(X | k and n) = 1
    # P(X | m and m) = 0.75
    # P(X | m and n) = 0.5
    # P(X | n and n) = 0

    return p_k_k + p_k_m + p_k_n + p_m_m * 0.75 + p_m_n * 0.5 + p_n_n * 0

print(p_dominant(2,2,2))