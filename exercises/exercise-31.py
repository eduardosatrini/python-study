# Print the first prime numbers below 20

def is_prime(num):
	for i in range(2, num):
		if not(num % i):
			return False # not prime
	return True # is prime

for num in range(1, 20):
	if is_prime(num):
		print(f"Prime: {num}")

print("End program..")
