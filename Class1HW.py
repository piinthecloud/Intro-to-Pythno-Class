print('Popsicle Stick: Knock knock')
input_value = raw_input("Me:").lower()

if input_value == "who's there?" or input_value == "who is there?": 
	print ("Popsicle Stick: Orange")
	
	input_value2 = raw_input ("Me:")
	
	if input_value2 == "Orange who?" or input_value2 == "orange who?": 
		print ("Popsicle Stick: Orange you gonna let me in??")
	else:
		print ("Try again..!")

else:
	print ("Try again!")
  