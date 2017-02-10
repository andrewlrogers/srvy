from gpiozero import Button
from time import sleep
import random
from signal import pause

print('initializing variables')
like = Button(18)
okay = Button(14)
dislike = Button(15)
score= 1
responses = 1.0 # the number of responses - must be float
questions = ['Did you enjoy your visit today?', 'Would you reccomend us to a friend?', 'Were you satisfied with the service you received today', 'Were you able to find what you were looking for?']
#pull questions from csv file on dropbox, run daily at midnight. From a different script. Q's stored as CSV.

def liked(score, qs, responses):
	print('Like')
	score = score +1 #weighted value of answer
	responses = responses+1
	sleep(.5) #prevents multiple presses
	#add time, qs, and score to db
	main(score, responses)

def okayed(score, qs, responses):
	print('I dont really care')
	responses = responses+1
	sleep(.5)
	main(score, responses)

def disliked(score, qs, responses):
	print('I hate life')
	score = score -1
	responses = responses+1
	sleep(.5)
	main(score, responses)

def main(score, responses):
	qs = random.choice(questions)
	weight = (score/responses)*100
	print(qs, weight)
	while True:
		if like.is_pressed:
                        liked(score, qs, responses)
                elif okay.is_pressed: 
			okayed(score, qs, responses)
                elif dislike.is_pressed:
			disliked(score, qs, responses)



main(score, responses)

