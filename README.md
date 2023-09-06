# sieve-eratosthenes-radix
Algorithim for Sieve of Eratosthenes with Radix sort for Non Prime numbers.
## Speed Improvements

This implementation of the Sieve of Eratosthenes leverages radix sort as a key optimization, resulting in significant speed improvements:

1. **Radix Sort Efficiency**: Radix sort is a linear-time sorting algorithm, which means its time complexity is O(n), where n is the number of elements to be sorted. In the context of the Sieve of Eratosthenes, radix sort is applied iteratively as the number of digits increases, making it more efficient compared to other sorting algorithms.

2. **Reduced Time Complexity**: The traditional Sieve of Eratosthenes has a time complexity of O(n log log n). However, by incorporating radix sort, this implementation reduces the overall time complexity, resulting in faster execution times for marking prime and non-prime numbers.

3. **Optimized Memory Usage**: Radix sort is known for its stable memory usage. It doesn't require additional memory allocation proportional to the input size, which can be advantageous for large ranges of numbers. This optimized memory usage contributes to the overall efficiency of the algorithm.

4. **Parallel Processing Potential**: Radix sort can be parallelized easily since it operates on individual digits independently. This means that for systems with multiple processing cores, the algorithm can take advantage of parallelism, further improving its speed for very large ranges.

5. **Reduced Redundant Marking**: Radix sort minimizes redundant marking of numbers. It ensures that each number is marked as prime or non-prime only once, reducing unnecessary iterations and computations.

Overall, the combination of the Sieve of Eratosthenes with radix sort leverages the efficient sorting properties of radix sort to make the prime number detection process faster and more scalable, especially when dealing with large upper limits (n). This approach can significantly improve the performance of prime number generation algorithms.

## Attribution

- **Sieve of Eratosthenes**: The core concept of prime number detection is based on the ancient algorithm devised by Eratosthenes.

- **Radix Sort**: The radix sort implementation used in this project was adapted from Harold H. Seward with modifications for this specific use case.

- **Inspiration**: The implementation was inspired by my own personal frustrations of not finding them fast enough.
  
