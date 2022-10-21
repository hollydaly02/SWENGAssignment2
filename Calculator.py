from collections import deque

# dictionary to help check precedence
Precedence = {'+':1, '-':1, '*': 2}												

# Function that takes an infix expression and returns it in postfix form.
def convertToPostfix(infix):

	output = ""
	stack = deque()																
	infix = infix.replace(' ', '')		

	for c in infix:
		if c.isdigit(): 									
			output += c
		else:																
			output += " "			
			# check for precedence and add to output
			while len(stack) > 0 and Precedence[c] <= Precedence[stack[-1]]:	
				output = output + stack.pop() + " "
			stack.append(c)

	# pop remaining operators and add to output
	while stack:																
		output = output + " " + stack.pop()
		
	return output

# Function that takes a postfix expression and returns the result.
def solvePostfix(postfix):
	argumentStack = deque()
	for symbol in postfix.split(" "):
		if symbol == "+":
			arg1 = argumentStack.pop()
			arg2 = argumentStack.pop()
			argumentStack.append(arg1+arg2)
		elif symbol == "-":
			arg1 = argumentStack.pop()
			arg2 = argumentStack.pop()
			argumentStack.append(arg2-arg1)
		elif symbol == "*":
			arg1 = argumentStack.pop()
			arg2 = argumentStack.pop()
			argumentStack.append(arg1*arg2)
		else:
			argumentStack.append(int(symbol))
	return argumentStack.pop()	

if __name__ == "__main__":
	try:
		inputExpression = input("Enter expression> ")
		answer = solvePostfix(convertToPostfix(inputExpression))
		print("The answer is {}".format(answer))
	except:
		print("Error, please input a valid expression")
		
