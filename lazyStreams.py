import os, sys 
from random import randint
import itertools

class random():
	def popNext(self):
		while True:
			randNum = randint(0,9)
			yield randNum

	def popN(self, num):
		s = self.popNext()
		for i in range(num):
			print s.next()

class primes():
	def popNext(self):
		current = itertools.count(2)
		while True:
			n = current.next()	
			current = itertools.ifilter(lambda x,n=n:x%n, current) 
			yield n

	def popN(self, num):
		s = self.popNext()
		for i in range(num):
			print s.next()

class primeFactors():
	def __init__(self, n):
		self.number = n

	def popNext(self):
		try:
			p = primes()
			pr = p.popNext()
			current = pr.next()
			while current <= self.number:
				if self.number % current == 0:
					yield current
					self.number /= current
				else:
					current = pr.next()
		except StopIteration:
			pass

	def popN(self, num):
		try:
			s = self.popNext()
			for i in range(num):
				print s.next()
		except StopIteration:
			pass

def map(fn, stream):	
	try:
		s = stream.popNext()
		while True:
			yield fn(s.next())
	except StopIteration:
		pass

def filter(fn, stream):
	try:
		s = stream.popNext()
		while True:
			e = s.next()
			if fn(e):
				yield e
	except StopIteration:
		pass

def zipWith(fn, streamA, streamB):
	try:
		sA = streamA.popNext()
		sB = streamB.popNext()
		while True:
			yield fn(sA.next()), fn(sB.next())
	except StopIteration:
		pass

def prefixReduce(fn, stream, init):
	try:
		current = init
		s = stream.popNext()
		while True:
			current = fn(current, s.next())
			yield current
	except StopIteration:
		pass

# test random integer
print "Printing 5 random elements"
r = random()
r.popN(5)

# test prime numbers
print "\nPrinting 5 prime numbers"
p = primes()
p.popN(5)

# test prime factors
print "\nPrinting prime factors of 90"
f = primeFactors(90)
f2 = primeFactors(90)
# test popping N elements
f2.popN(5)

# test mapping
print "\nTesting map function on x*2"
for i in map((lambda x: x*2), f):
	print i

# test filtering
print "\nTesting filter function on x%3"
for i in filter((lambda x: x%3==0), primeFactors(90)):
	print i

# test zipWith
print "\nTesting zipWith function on x"
for i in zipWith((lambda x: x), primes(), primeFactors(90)):
	print i

# test prefixReduce
print "\nTesting prefix reduce function on x+y, init with 2"
for i in prefixReduce((lambda x, y: x+y), primeFactors(90), 2):
	print i
