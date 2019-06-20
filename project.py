ques1="""ques1: You are on a holiday. what you will decide to do?? 
a.go for a longdrive. *
b.go on a date.
c.SLEEP whole day."""
ques2=""" ques2:You want to go on a long drive.choose and option.
a.by bus
b.by car. *
c.not in a mood."""
ques3=""" ques3:where you want to go.choose further options.
a.goa
b.shimla.
c. kahi bhi chle jayenge. * """
ques4=""" ques4:What will you do in case of earthquake??
a.just let it pass. *
b. find an elephant.
c.hide under a table."""
ques5=""" ques5:Your parents don't allow you to go anywhere. what will you do?/
a.do nothing.
b. Request them .*
c.go without seeking permission."""
ques6=""" ques6:you are having one pizza .what uh do?/
a.share with one of you friend.
b.ask them if he/she want to eat.
c.PIZZA IS NOT for SHARING..hha.* """
ques7=""" ques7:what will you choose??
a.family. *
b.true love
c.100 million dollars."""
ques8=""" ques8:if you can control one thing what it would be.
a.time
b.money.*
c.feelings."""
ques9="""ques9:If you were walking through a forest and you suddenly saw a tiger,what uh do>??
a.run as fast as possible.
b.climb a tree
c. lay down.*"""

question={"question2":ques2, "question 3":ques3, "question 4":ques4, "question 5":ques5, "question 6":ques6, "question7":ques7, "question 8":ques8, 
           "question 9":ques9}
print(ques1)
answers=['a','b','c','a','b','c','a','b','c']
user_answer=input("your answer").lower()
for item in question.values():
	for correct_answer in answers:
		if user_answer==correct_answer:
			print("correct answer")
			print(item)
		user_answer=input("your answer")
		answers.pop(0)
		break
	else:
		print("wrong answer")
		quit()

