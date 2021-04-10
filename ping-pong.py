from pygame import *
from random import randint
from time import time as timer 
 
#музло
mixer.init()
mixer.music.load('muzlo.mp3')
mixer.music.play()

#картинки
racket = 'racket.png'
ten_ball = 'tenis_ball.png'
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
#конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed,size_x, size_y):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс главного игрока
class Player(GameSprite):
  #метод для управления спрайтом стрелками клавиатуры
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    
back = (0,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)

#фонты и переменные
sc1 = 0
sc2 = 0
font.init()
font1 = font.SysFont('Calibri', 50)
win1 = font1.render('Player 1 win!',True,(255,0,0))
win2 = font1.render('Player 2 win!',True,(255,0,0))



#игроки
player1 = Player(racket,30,200,4,50,150)
player2 = Player(racket,520,200,4,50,150)
ball = GameSprite(ten_ball,200,200,2,50,50)

run = True
finish = False

speed_x = 4
speed_y = 4

FPS = 60
clock = time.Clock()

while run:
    last_time = timer()
    #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    last_time = timer()

    if not finish:

        score_p1 = font1.render(str(sc1),True,(255,255,0))
        score_p2 = font1.render(str(sc2),True,(255,255,0))

        player1_text = font1.render('1',True,(0,0,255))
        player2_text = font1.render('2',True,(255,0,0))

        window.fill(back)
        player1.update_right()
        player2.update_left()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        window.blit(score_p1,(200,0))
        window.blit(score_p2,(410,0))

        window.blit(player1_text,(100, 50))
        window.blit(player2_text,(450, 50))

        if sprite.collide_rect(ball,player1):
            speed_x *= -1
            sc1 += 1
        if sprite.collide_rect(ball,player2):
            speed_x *= -1
            sc2 += 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(win2,(200,200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(win1,(200,200))
        
        player1.reset()
        player2.reset()
        ball.reset()
        now_time = timer()
        if now_time - last_time >= 181:
            mixer.music.play()

    
    display.update()
    clock.tick(FPS)