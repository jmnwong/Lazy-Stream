Implementation of a lazy stream in Python.

There are three stream classes that are lazily implemented:
1. Random - Returns a stream of unique random numbers between 0-9
2. Primes - Returns a stream of prime numbers in order
3. PrimeFactors - Returns a stream of prime factors given an integer N

Higher-order functions are also implemented:
1. map(fn, stream) - Returns a stream where fn has been applied to each element.
2. filter(fn, stream) - Returns a stream containing only the elements for which fn returns True.
3. zipWith(fn, streamA, streamB) - Applies a given binary function pairwise to elements of two given lists.
4. prefixReduce(fn, stream, init) - Applies a reduction on the stream with fn(x,y)

Each class also implements the popN(num) function which pops up to num elements
