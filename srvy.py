from gpiozero import Button
from time import sleep

print('initializing variables')
like = Button(18)
okay = Button(14)
dislike = Button(15)



def main():
        score = 0
        while True:
                if like.is_pressed:
                        print('like')
			score = score + 1
			sleep(.5)
			print(score)
                elif okay.is_pressed:
                        print('okay')
			sleep(.5)
			print(score)
                elif dislike.is_pressed:
			score = score - 1
                        print('disliked')
			sleep(.5)
			print(score)

main()

