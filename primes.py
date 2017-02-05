# Lets find the largest prime possible
# This program will print out prime numbers, sexy primes, and triple sexy primes

def is_prime(prime):
    for i in range(2, int(prime/2)+1):
        if prime % i == 0:
            return False
    return True

# Change this to the largest prime number you know
highest_prime = 0 + 1
counter = 0
double_counter = 0
triple_counter =  0
while (True):
    if is_prime(highest_prime):
        print("#" + str(counter) + ": " + str(highest_prime))
        counter = counter + 1
        if is_prime(highest_prime + 6):
        	print("#" + str(double_counter) + ": (" + str(highest_prime) + ", " + str(highest_prime+6) + ")")
        	double_counter = double_counter + 1
        	if is_prime(highest_prime - 6):
        		if not(is_prime(highest_prime - 5) or is_prime(highest_prime -4) or is_prime(highest_prime -3) or is_prime(highest_prime -2) or is_prime(highest_prime-1)):
           			if not(is_prime(highest_prime + 5) or is_prime(highest_prime +4) or is_prime(highest_prime +3) or is_prime(highest_prime +2) or is_prime(highest_prime +1)):
           				print("#" + str(triple_counter) + ": (" + str(highest_prime-6) +  ", " + str(highest_prime) + ", "+str(highest_prime+6)+")")
                		triple_counter = triple_counter + 1
    highest_prime = highest_prime + 1
    
    
