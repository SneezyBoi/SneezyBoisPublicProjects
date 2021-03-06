import math
import time
import random
from random import randrange
'''
This program is made to simulate the accuracy of the equation:
([3+4N]**2)-2

It will work by generating results up to the specified Nth term in
the equation "10**N", checking if each result is prime, and if
it is prime, adding it to a tally to be divided by the equation
"10**N".
'''

N = int(input("N: "))
modifier = int(input("Modifier (LD=2): "))

start = time.time()

amntofprimes = 0
result = 0
i = 0

def spacemaker(spaces):
    for spacecounter in range(spaces):
        print("")

def percentage(numerator, denominator):
    percent = (numerator/denominator) * 100
    percent = round(percent, 6)
    return percent

def miller_rabin(n, k=10):
	if n == 2:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in range(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in range(k):
		a = randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True

def is_prime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True


for integer in range(1,N+1):

    #print(integer)
    i = i + 1
    if i % 100 == 0:
        print(percentage(integer,N))

'''
YOUR EQUATION IS WHAT "result" IS EQUAL TO
'''

    result = (YOUR EQUATION HERE)
    if miller_rabin(result) == True:
        amntofprimes = amntofprimes + 1
    else:
        amntofprimes = amntofprimes

totaloutofone = float(amntofprimes/N)

spacemaker(20)

print("Accuracy (Decimal): " + str(totaloutofone))

end = time.time()
print("Time: " + str(end - start))
print("N Value: " + str(N))
print("M Value: " + str(modifier))
