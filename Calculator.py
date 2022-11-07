from collections import deque

from flask import Flask, render_template, request
app = Flask(__name__)

# dictionary to help check precedence
Precedence = {'+':1, '-':1, '*': 2, '/': 2, '^': 3}			

@app.route("/")
def homeFormPage():
	return render_template('home-form.html')
							

def convertToPostfix(infix):

	output = ""
	stack = deque()																
	infix = infix.replace(' ', '')		

	for c in infix:
		if c.isdigit(): 									
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
		if symbol.isdigit():
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
