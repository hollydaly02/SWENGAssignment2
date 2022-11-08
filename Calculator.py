from collections import deque
import math

from flask import Flask, render_template, request
app = Flask(__name__)

# dictionary to help check precedence
Precedence = {'+':1, '-':1, '*': 2, '/': 2, '^': 3}			

@app.route("/")
def homeFormPage():
	return render_template('home-form.html')
							

# returns array with evaluated exp in index 0, and the exp expression itself in index 1
def evalExp(input, index):
	output = []
	string = input
	startIndex = index
	endIndex = startIndex + 4
	exp = ""
	while string[endIndex] != ")":
		exp += string[endIndex]
		endIndex += 1
	x = math.exp(float(exp))
	x = round(x, 3)
	output.append(str(x))
	output.append(string[startIndex:endIndex+1])
	return output



def evalLog(input, index):
	output = []
	string = input
	startIndex = index
	endIndex = startIndex + 4
	log = ""
	while string[endIndex] != ")":
		log += string[endIndex]
		endIndex += 1
	x = math.log(float(log))
	x = round(x, 3)
	output.append(str(x))
	output.append(string[startIndex:endIndex+1])
	return output


# method to replace all exps and logs in original string with evaluated answers 
def replaceExpExpression(string):
	output = ""

	numOfExp = string.count("exp")
	for i in range(numOfExp):
		if output == "":
			expIndices = [x for x in range(len(string)) if string.startswith("exp(", x)]
			x = evalExp(string, expIndices[0])
			output = string.replace(x[1], x[0])
		else:
			expIndices = [x for x in range(len(output)) if output.startswith("exp(", x)]
			x = evalExp(output, expIndices[0])
			output = output.replace(x[1], x[0])
	return output

# method to replace all exps and logs in original string with evaluated answers 
def replaceLogExpression(string):
	output = ""

	numOfExp = string.count("log")
	for i in range(numOfExp):
		if output == "":
			logIndices = [x for x in range(len(string)) if string.startswith("log(", x)]
			x = evalLog(string, logIndices[0])
			output = string.replace(x[1], x[0])
		else:
			logIndices = [x for x in range(len(output)) if output.startswith("log(", x)]
			x = evalLog(output, logIndices[0])
			output = output.replace(x[1], x[0])
	return output
 

# method to check if input is float
def checkFloat(input):
	try:
		float(input)
		return True
	except ValueError:
		return False



def convertToPostfix(infix):
	#find log/exp, evaluate and replace it in the original infix string
	
	if "exp" in infix:
		infix = replaceExpExpression(infix)
	if "log" in infix:
		infix = replaceLogExpression(infix)
	output = ""
	stack = deque()																
	infix = infix.replace(' ', '')		

	for c in infix:
		if c.isdigit() or c == '.': 									
			output += c

		elif c == '(':
			stack.append(c)
		
		elif c == ')':
			while (stack[-1] != '(') and (stack):
				output = output + " " + stack.pop()
			
			stack.pop()

		else:																
			output += " "			
			# check for precedence and add to output
			while  len(stack) > 0 and stack[-1] != '(' and Precedence[c] <= Precedence[stack[-1]]:	
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
		if symbol.isdigit() or checkFloat(symbol):
			argumentStack.append(symbol)
		else:
			arg1 = argumentStack.pop()
			arg2 = argumentStack.pop()
			
			if symbol == "^":
				answer = float(arg2) ** float(arg1)
			
			else:
				answer = eval(arg2 + symbol + arg1)
			
			argumentStack.append(str(answer))
	# this sends out the answer page for the front end, with the new calculated variables
	#return render_template('answer-page.html', postfixEquation = postfix, answer = argumentStack.pop())
	
	return round(float(argumentStack.pop()), 3)


# Function that takes an infix expression and returns it in postfix form.
@app.route("/", methods=['POST'])
def takeInfix():
	infix = request.form['text']
	try:
		postfix = convertToPostfix(infix)
		return render_template('answer-page.html', postfixEquation = postfix, answer = solvePostfix(postfix))
	except:
		return render_template('error-page.html')
	


if __name__ == 'main':
	app.run(host="0.0.0.0", port=5000)
