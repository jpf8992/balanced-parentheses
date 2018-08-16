
def determineBalanced( inputString ):

	print("Processing: " , inputString)
	queue =[]
	
	# Remove all unecessary characters form string
	for character in inputString:
		if (character is  "(" or character is ")"):
			queue.append(character)


	opening_brace = "("
	closing_brace = ")"
	balance_list = []

	# Push/pop to stack for balance
	for brace in queue:

		if (brace == opening_brace):
			balance_list.append(brace)
			print("Pushed Open Brace", balance_list)

		elif (brace == closing_brace and balance_list):
			balance_list.pop()
			print("Popped Closed Brace" , balance_list)

		else:
			print("Unbalanced")
			return 1

	if not balance_list:
		print("Balanced")
	else:
		print("Unbalanced")
	


def main():

	print("In main")

	with open('sampleText.txt','r') as inputFile:
		data = inputFile.read()

	# Process input string
	# Could be made to handle all manner of parentheses e.g. [{}]
	determineBalanced(data)




if __name__ == "__main__":

	main()