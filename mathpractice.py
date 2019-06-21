import sys
#parses user input
def u_in():
	n = input("what is you number? ")
	try:
		num = int(n)
		if num > 1:			
			return num
	except ValueError:
		print("invalid input. try again")
		u_in()

#finds primes and handles all cases.
def prime(num):
	primes = []
	#takes a range of numbers 
	#	TODO: handles a list of numbers maybe. Not necessary but I should at the least handle the case.
	for i in range(2, num):
		#starts at 2 as all numbers are divisible by one. ony goes up to the range of var i + 1
		for j in range(2,i + 1):
			#I like mod
			result = (i % j)
			#Must go through all number from 2-n+1.
			if (i == j): #was checking result == 1 but I didn't need to. 
				primes.append(i)
			#starting at 2(common divisible) if remainder is 0. try next number
			elif result == 0:
				break
	return primes
#There seems to be a lot that can be tightened up here. 
def main(): 
	if len(sys.argv) > 1:
		t = sys.argv[1:]
		for i in t:
			if int(i) < 1:
				print("number not valid. try again")
			else:
				prime(int(i))
	else:
		prime(u_in())

if __name__ == '__main__':
	main()

