from Calculator import convertToPostfix, solvePostfix

# Tests for convertToPostfix.
def testConvertToPostfix():

	assert convertToPostfix("5 - 10") == "5 10 -"
	assert convertToPostfix("150 + 25 * 30") == "150 25 30 * +"
	assert convertToPostfix("10 + 15 * 5 - 7") == "10 15 5 * + 7 -"
	assert convertToPostfix("23 * 2 + 80 * 60") == "23 2 * 80 60 * +"
	assert convertToPostfix("60 * 2 * 70 - 90") == "60 2 * 70 * 90 -"



# Tests for solvePostfix.
def testSolvePostfix():
	assert solvePostfix("2 4 +") == 6
	assert solvePostfix("3 3 *") == 9
	assert solvePostfix("9 6 -") == 3
	assert solvePostfix("4 3 * 12 + 4 -") == 20
