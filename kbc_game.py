print("<<<<<<<<<<<< WELCOME TO KBC GAME >>>>>>>>>>>>>\n\n         [ * KON BANEGA CROREPATI * ]")
print()
f=int(input("Press 1 to start KBC game: "))
if f==1:
	print()
	print("Note. 1. You will get 10 questions and for each questions you will get four option.\n      2. You will also get 50 50 lifeline.")
	print()
	g=int(input("Press 2 for see questions: "))
	if g==2:
		print()
		print()
		print("    <<<<<<<<<< This your questions >>>>>>>>>>"    )
		print()
		print()
q = [
	"Q1. How many continents are there?",
	"Q2. What is the capital of India?",	
	"Q3. NG mei kaun se course padhaya jaata hai?",
	"Q4. Which State in India is the largest producer of Soyabean?",
	"Q5. Which day is observed as the World Standards  Day?",
	"Q6. The world smallest country is",
	"Q7. Which one of the following was the first fort constructed by the British in India?",
	"Q8. What is the second largest country (in size) in the world?",
	"Q9. The state which has the largest number of sugar mills in India is",
	"Q10.Which language is spoken in Karnataka?",


]
op = [
	"a. Four\nb. Nine\nc. Seven\nd. Eight",
	"a. Chandigarh\nb. Bhopal\nc. Chennai\nd. Delhi",
	"a. Software Engineering\nb. Counseling\nc. Tourism\nd. Agriculture",
	"a. Rajasthan\nb. Gujarat\nc. Uttar Pradesh\nd. Madhya Pradesh",
	"a. June 26\nb. Oct 14\nc. May 21\nd. April 2",
	"a. Canada\nb. Russia\nc. Maldives\nd. Vatican City",
	"a. Fort William\nb. Fort St. George\nc. Fort St.David\nd. Fort St.Angelo",
	"a. Canada\nb. USA\nc. Chinawrong\nd. Russia",
	"a. Bihar\nb. Haryana\nc. Punjab\nd. Uttar Pradesh",
	"a. Marathi\nb. Hindi\nc. Malayalam\nd. Kannada",
]
s=["c","d","a","d","b","d","b","a","d","d"]
_50_50_option=[
			"c. Seven\nd. Eight",
			"a. Chandigarh\nd. Delhi",
			"a. Software Engineering\nb. Counseling",
			"c. Uttar Pradesh\nd. Madhya Pradesh",
			"a. June 26\nb. Oct 14",
			"c. Maldives\nd. Vatican City",
			"b. Fort St. George\nc. Fort St.David",
			"a. Canada\nb. USA",
			"c. Punjab\nd. Uttar Pradesh",
			"c. Malayalam\nd. Kannada"]
count=0
m=0
option=0
for i in q:
	print(q[m])
	print()
	print(op[m])
	print()
	if count==0:
		a=input("If you wants 50 50 life line enter yes/no: ")
		if a=="yes":
			print()
			print(_50_50_option[option])
			print()
			b=input("Choose your option: ")
			count+=1

			if b==s[option]:
				print()
				print("Congratulations! You are choosen a perfect option:\n\nWarning: Now, you can't use 50 50 lifeline any more:")
				print()
			else:
				print()
				print("Sorry! You lost your 50 50 lifeline chance and get out from KBC:")
				print()
				break
		else:
			print()
			c=input("Choose your option: ")
			print()
			if c==s[option]:
				print()
				print("Congratulations! Your answer is correct:")
				print()
			else:
				print()
				print("Sorry! You are choosen a wrong option and get out from KBC:")
				print()
				break
	elif count>0:
		c=input("Choose your option: ")
		if c==s[option]:
			print()
			print("Congratulations! Your answer is correct:")
			print()
		else:
			print()
			print("Sorry! You are choosen a wrong option and get out from KBC:")
			print()
			break
	m+=1
	option+=1
