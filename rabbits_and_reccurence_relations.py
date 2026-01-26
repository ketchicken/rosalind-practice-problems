"""
Given: Positive integers n≤40 and k≤5

Return: The total number of rabbit pairs that will be present after n
 months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
 rabbit pairs (instead of only 1 pair). 

 Rabbits mature after 2 months. Fibonacci.
"""

def rabbit_pairs_after_n_months(generations:int, litter:int)->int:
    if generations <= 1: 
        return generations

    # rabbits from n-2 months ago will have a litter
    return rabbit_pairs_after_n_months(generations-1, litter) + rabbit_pairs_after_n_months(generations-2, litter) * litter

print(rabbit_pairs_after_n_months(31, 5))