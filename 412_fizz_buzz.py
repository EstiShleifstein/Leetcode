from typing import List

#INSTRUCTIONS:
# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.


def fizz_buzz_1(n: int) -> List[str]:
	"""

	Solution 1. 

	One-liner, but not the best runtime (43ms), since the list comprehension makes it that each part has to be evaluated each time.

	Implemented list comprehension to input appropriate string based on the mod that the number did or did not evaluate to. 
		
	"""
	return ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, n+1)]

# Solution 2
def fizz_buzz_2(n: int) -> List[str]:
	"""
	Solution 2:

	Most straightforward way of going about question. Appending the appropriate value using conditional logic.

	"""
	result = ['1', '2']
	for num in range(3, n + 1):
		if num % 3 == 0 and num % 5 == 0:
			result.append("Fizzbuzz")
		elif num % 3 == 0:
			result.append("fizz")
		elif num % 5 == 0:
			result.append("buzz")
		else:
			result.append(str(num))
	return result

    
print(fizz_buzz_1(15))
print(fizz_buzz_2(15))

	
                