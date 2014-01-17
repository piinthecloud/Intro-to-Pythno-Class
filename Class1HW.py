print('Popsicle Stick: Knock knock')
input_value = raw_input("Me:")


if input_value == "Who's there?" or input_value == "Who is there?" or input_value == "who's there?" or input_value == "who is there?": 
	print ("Popsicle Stick: Orange")
	input_value2 = raw_input ("Me:")
	
	if input_value2 == "Orange who?" or "orange who?": 
		print ("Popsicle Stick: Orange you gonna let me in??")
	else:
		print ("Try again..!")
else:
	print ("Try again!")



