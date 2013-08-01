'''
http://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

def isDivisibleByAll20(num):
   retVal = True
   for i in xrange(1,21):
      if (num % i) != 0:
         retVal = False
   return retVal
# create a hash table with all primes below 20.
# create an array of length 20, initialized to zero

commonFactorCount = [0] * 20


#factor all numbers below 20.
for i in range(2,21):
   curFactorCount = [0] * 20;
   print "factors of"+str(i)+":",
   iTemp = i
   for factor in range(2,iTemp+1):
      while iTemp % factor == 0:
         print "\t"+str(factor),
         curFactorCount[factor] += 1
         iTemp = iTemp / factor
   print ""
   for factor in range(2,i):
      if curFactorCount[factor] > commonFactorCount[factor]:
         commonFactorCount[factor] = curFactorCount[factor]

# count the numbers in each factor, putin hash table

#multiply all the stuff in the hash table together. 

# that's near linear-ish. Not quadratic anyway.





