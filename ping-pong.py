from pygame import *
from random import randint
from time import time as timer 
 

#картинки
racket = 'racket.png'
ten_ball = 'tenis_ball.png'
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
#конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
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
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    
back = (0,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)

#фонты
font.init()
font1 = font.SysFont('Calibri', 50)
win1 = font1.render('Player 1 win!',True,(255,0,0))
win2 = font1.render('Player 2 win!',True,(255,0,0))

#игроки
player1 = Player(racket,30,200,50,150,4)
player2 = Player(racket,520,200,50,150,4)
ball = GameSprite(ten_ball,200,200,50,50,4)

run = True
finish = False

speed_x = 3
speed_y = 3

FPS = 60
clock = time.Clock()

while run:
    #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        window.fill(back)
        player1.update_left()
        player2.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(ball,player1) or sprite.collide_rect(ball,player2):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y < win_height-50 or ball.rect.y < 0:
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

    display.update()
    clock.tick(FPS)