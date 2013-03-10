# Lazy Stream Implementation in Python

There are three stream classes that are lazily implemented:
- Random - returns a stream of unique random numbers between 0-9
- Primes - returns a stream of prime numbers in order
- PrimeFactors - returns a stream of prime factors given an integer *N*

Higher-order functions are also implemented:
- `map(fn, stream)` - returns a stream where fn has been applied to each element.
- `filter(fn, stream)` - returns a stream containing only the elements for which `fn` returns `True`.
- `zipWith(fn, streamA, streamB)` - applies a given binary function pairwise to elements of two given lists.
- `prefixReduce(fn, stream, init)` - applies a reduction on the stream with `fn(x,y)`

Each class also implements the `popN(num)` function which pops up to num elements
