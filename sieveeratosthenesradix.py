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
        # Counting sort to mark numbers as prime or not
        count = [0] * 10
        for num in range(n + 1):
            digit = (num // exp) % 10
            count[digit] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        temp = [0] * (n + 1)
        i = n
        while i >= 0:
            digit = (i // exp) % 10
            if is_prime[i] and digit != 0:
                # i is prime, mark its multiples as not prime
                for j in range(2 * i, n + 1, i):
                    is_prime[j] = False
            temp[count[digit] - 1] = i
            count[digit] -= 1
            i -= 1

        for i in range(n + 1):
            temp[i] = is_prime[temp[i]]  # Update temp based on is_prime

        for i in range(n + 1):
            is_prime[i] = temp[i]  # Copy the updated values back to is_prime

        exp *= 10

    # Return a list of nonprime numbers
    nonprimes = [i for i in range(n + 1) if is_prime[i]]
    return nonprimes

if __name__ == "__main__":
    n = 200
    nonprime_list = sieve_eratosthenes_radix(n)
    print("Non Prime numbers up to", n, "are:", nonprime_list)