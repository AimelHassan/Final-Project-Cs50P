import pygame
import os
import random
import functions
import sys
pygame.font.init()
pygame.mixer.init()
pygame.init() #turn all of pygame on.
#The dimensions of the window
WIDTH, HEIGHT = 500,300

FPS = 60

#COLORS
WHITE = 255,255,255
BLACK = 0,0,0

font = pygame.font.SysFont('SKYGRAZE', 20)

Crosshair = pygame.image.load(os.path.join('Assets', 'Crosshair.png'))
TARGET_IMG = pygame.image.load(os.path.join('Assets', 'Target.png'))
SCREEN_IMG = pygame.image.load(os.path.join('Assets', 'screen_img.png'))
LD_TEXT_IMG = pygame.image.load(os.path.join('Assets', 'leaderboard_text.png'))
BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'BG.jpg')), (WIDTH, HEIGHT))

screen = pygame.transform.scale(SCREEN_IMG, (WIDTH, HEIGHT))
TARGET = pygame.transform.scale(TARGET_IMG, (75, 75))
ld_text = pygame.transform.scale(LD_TEXT_IMG, (126,200))

BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Gun-Silencer.wav')
GAME_START_SOUND = pygame.mixer.Sound('Assets/Game start.wav')

leaderboard = functions.Leaderboard()

def main():
    global WIN
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("AIM TRAINER")
    current_time = 0
    hits = []
    Screen = pygame.Rect((0,0),(WIDTH,HEIGHT))
    target = pygame.Rect((220, 100), (38, 38))
    button = pygame.Rect((145,188),(200,30))
    clock = pygame.time.Clock()
    run = True
    button_click_time = 100000
    while run:
        mouse= pygame.mouse.get_pos()
        key_pressed = pygame.key.get_pressed() 
        clock.tick(FPS)         
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and pygame.K_s:
                    Screen.x, Screen.y = 1000,10000
                    button.x,button.y = 1000,1000
                    GAME_START_SOUND.play()
                    button_click_time = pygame.time.get_ticks()
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if target.collidepoint(mouse):
                    BULLET_HIT_SOUND.play()
                    hits.append(".")
                    target.x = random.randint(10,450)
                    target.y = random.randint(10,250)
                if button.collidepoint(mouse):
                    leaderboard.show()

      
            if key_pressed[pygame.K_r]:
                _restart()
        dis_time = current_time-button_click_time
        points = functions.point_calc(hits)
        draw_window(target,Screen,screen,button,points,dis_time)
        if current_time - button_click_time >= 10000:
            run = False
        


    functions.user_get_store(points)

    leaderboard.create()
    print("game end")
    pygame.quit()



def draw_window(target,Screen,screenimg,button, points,dtime):
    time = dtime//1000
    WIN.blit(BG_IMG, (0,0))

    points_text = font.render("Points: " +str(points),1,WHITE)
    WIN.blit(points_text, (20,10))
    time_text = font.render("Time: " +str(time),1,WHITE)
    WIN.blit(time_text,(380,10))

    WIN.blit(TARGET,(target.x-20,target.y-15))

    pygame.draw.rect(WIN,BLACK,Screen)
    WIN.blit(screenimg,(Screen.x,Screen.y))    
    WIN.blit(LD_TEXT_IMG,(button.x,button.y))

    #change the cursor to crosshair
    pygame.mouse.set_visible(False)
    Crosshair_rect = Crosshair.get_rect()    
    Crosshair_rect.center = pygame.mouse.get_pos()  # update position        
    WIN.blit(Crosshair, Crosshair_rect) # draw the cursor
 
    pygame.display.update()



def _restart():
    main()
    


if __name__ == "__main__":
    main()

