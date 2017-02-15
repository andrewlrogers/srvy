import pygame
import random


pygame.init()
screen_width=800 #Set width and height to match your monitor.
screen_height=480
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False) # Hides the mouse cursor
done = False

question = random.choice(['Did you enjoy your visit today?', 'Would you reccomend us to a friend?', 'Were you satisfied with the service you received today?', 'Were you able to find what you were looking for?'])
bg_color = random.choice([(105, 58, 119), (162, 173, 0), (125, 154, 170), (86, 90,92)]) #crocker colors


font = pygame.font.SysFont("Futura, Helvetica, Arial", 48) #system fonts and size
text = font.render(question, True, (255,255,255)) #text, anti-alias, color



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill(bg_color) #sets background color
    screen.blit(text, (screen_width/2 - text.get_rect().width/2,screen_height/2)) #adds text to
    pygame.display.flip()
    #clock.tick(10)
