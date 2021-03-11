i = 1
#increment counter 
while i <= 100:
#if number is divisble by 3, print out fizz
	if i%3==0:
		print("Fizz", end="")
		#if number is divisible by 5, print Buzz
		if i%5==0:
			print("Buzz", end="")
			#if its both then prints out fizzbuzz
	elif i%5==0:
		print("Buzz", end="")
	else:
	#just prints out number if not divisible by either
		print(i, end="")
	print()
	i+=1