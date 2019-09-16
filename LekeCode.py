# This is a random password generator


import random

selection1 = "qwertyuiopasdfghjklzxcvbnm"
selection2 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_+-[];'@:<>/?#!!£$%^&*"
length1 = 5
length2 = 12

def happy_check():
	loop_controller3 = 'true'
	while loop_controller3 == 'true':
		decision3 = input('Are you happy with your password?\n type:\n yes or no\n')
		if decision3 == 'no':
		    print('Ok lets try again.')
		    generate()
		elif decision3 == 'yes':
			print('Be sure to memorise your password\n Goodbye Human!')
			quit()
		else:
			print('PLEASE read instructions carefully')
			print('PLEASE TYPE! \nyes or no')
			loop_controller3 = 'true'


def generate():
	loop_controller1 = 'true'
	while loop_controller1 == 'true':
		decision2 = input('do you want a weak, medium or strong password\
			inputs: \nw --> weak\nm --> medium\ns --> strong\n')
		decision2.lower()
		if decision2 == 'w':
			output = "".join(random.sample(selection1,length1))
			print('PASSWORD --> ',output)
			happy_check()
			break
			#loop_controller1 = 'false'
		elif decision2 == 'm':
			output = "".join(random.sample(selection2,length1))
			print('PASSWORD --> ',output)
			happy_check()
			break
			#loop_controller1 = 'false'
		elif decision2 == 's':
			output = "".join(random.sample(selection2,length2))
			print('PASSWORD --> ',output)
			happy_check()
			break
			#loop_controller1 = 'false'
		else:
			print('PLEASE read instructions carefully\n TRY AGAIN')

loop_controller2 = 'true'
while loop_controller2 == 'true':
	decision1 = input('do you require my services human?\n type:\n yes or no\n')
	decision1.lower()

	if decision1 == 'no':
		print('goodbye human')
		loop_controller2 = 'false'
	elif decision1 == 'yes':
		generate()
		loop_controller2 = 'false'
	else:
		print('PLEASE read instructions carefully')
		print('PLEASE TYPE! \nyes or no')
