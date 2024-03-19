# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 01:47:43 2023

@author: Sean Smith
"""

def sieve_eratosthenes_radix(n):
    # Initialize a list of booleans to mark numbers as prime or not
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Using radix sort to iterate through numbers efficiently
    exp = 1
    while n // exp > 0:
        # Radix sort to mark numbers as prime or not
        temp = [0] * (n + 1)
        for num in range(n + 1):
            digit = (num // exp) % 10
            if is_prime[num] and digit != 0:
                # num is prime, mark its multiples as not prime
                for j in range(2 * num, n + 1, num):
                    is_prime[j] = False
            temp[num] = is_prime[num]

        for i in range(n + 1):
            is_prime[i] = temp[i]  # Copy the updated values back to is_prime

        exp *= 10

    # Return a list of nonprime numbers
    nonprimes = [i for i in range(n + 1) if not is_prime[i]]
    return nonprimes

if __name__ == "__main__":
    n = 200
    nonprime_list = sieve_eratosthenes_radix(n)
    print("Non Prime numbers up to", n, "are:", nonprime_list)
    
