''' 
Even Fibonacci numbers 
Problem 2 

	Each new term in the Fibonacci sequence is generated by adding the 
	previous two terms. By starting with 1 and 2, the first 10 terms 
	will be:
		1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
	By considering the terms in the Fibonacci sequence whose values do
	not exceed four million, find the sum of the even-valued terms.
'''

FIB_MAX = 4000000 # not exceed four million 
fibonacci = [1, 2]    # lista da sequência fibonacci 
result = 0
i = 2

while True:
	result = fibonacci[i - 1] + fibonacci[i - 2]
	fibonacci.append(result)
	if result > FIB_MAX:
		del fibonacci[i]
		break
	i += 1

print(fibonacci)

def sumEven(list_fib):
	sum_even = 1 # começa pelo número 1
	for i in range(len(list_fib)):
		if list_fib[i]%2 == 0: # se é ímpar 
			# do nothing
			print('c')
		else:
			sum_even = sum_even + list_fib[i]
	return sum_even 
				
print(sumEven(fibonacci)) # 4613732