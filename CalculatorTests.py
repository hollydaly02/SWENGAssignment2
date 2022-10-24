from Calculator import convertToPostfix, solvePostfix

# Tests for convertToPostfix.
def testConvertToPostfix():

	assert convertToPostfix("5 - 10") == "5 10 -"
	assert convertToPostfix("150 + 25 * 30") == "150 25 30 * +"
	assert convertToPostfix("10 + 15 * 5 - 7") == "10 15 5 * + 7 -"
	assert convertToPostfix("23 * 2 + 80 * 60") == "23 2 * 80 60 * +"
	assert convertToPostfix("60 * 2 * 70 - 90") == "60 2 * 70 * 90 -"

	# test for division and brackets

	assert convertToPostfix("10 + 2 + (2 * 5)") == "10 2 + 2 5 * +"
	assert convertToPostfix("124 / (10 - 5)") == "124 10 5 - /"
	assert convertToPostfix("25 - 5 * (8 / 4)") == "25 5 8 4 / * -"
	assert convertToPostfix("(12 * 8) - (12 / 3)") == "12 8 * 12 3 / -"



# Tests for solvePostfix.
def testSolvePostfix():
	assert solvePostfix("2 4 +") == 6.0
	assert solvePostfix("3 3 *") == 9.0
	assert solvePostfix("9 6 -") == 3.0
	assert solvePostfix("4 3 * 12 + 4 -") == 20.0

	# test for division and brackets

	assert solvePostfix("25 5 8 4 / * -") == 15.0
	assert solvePostfix("10 2 + 2 5 * +") == 22.0
	assert solvePostfix("12 8 * 12 3 / -") == 92
	assert solvePostfix("124 10 5 - /") == 24.8