from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y <= 500:
            self.rect.y += self.speed
        if key_pressed[K_a]:
            self.rect.x -= self.speed
        if key_pressed[K_d]:
            self.rect.x += self.speed

        
        
class Enemy(GameSprite):
    direction = 'right'
    def update(self):
        if self.rect.x <= 400:
            self.direction = 'right'
        if self.rect.x >= 600:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, r, g, b, x, y, w, h):
        super().__init__()
        self.red = r
        self.green = g
        self.blue = b
        self.width = w
        self.height = h
        self.image = Surface((self.width, self.height))
        self.image.fill((self.red, self.green, self.blue))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



clock = time.Clock()
window = display.set_mode((700, 500))
display.set_caption('Лабаиринт')
background = transform.scale(image.load('background.jpg'), (700, 500))


hero = Player('hero.png', 50, 50, 5)
cyborg = Enemy('cyborg.png', 300, 300, 3)
gold = GameSprite('treasure.png', 300, 400, 0)

w1 = Wall(154, 205, 50, 100, 20, 600, 10)
w2 = Wall(154, 205, 50, 100, 20, 10, 350)
w3 = Wall(154, 205, 50, 220, 150, 10, 600)
w4 = Wall(154, 205, 50, 220, 150, 300, 10)
w5 = Wall(r= 154, g= 205, b= 50, x=100, y=470, w=300, h= 10)


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()


font.init()
font = font.Font(None, 70)
win = font.render('Ты выйгал!', True, (225, 215, 0))
lose = font.render('Ты поиграл!', True, (180, 0, 0))



finish = False
game = True
while game:
    if finish != True:
        window.blit(background, (0, 0))
        hero.reset()
        cyborg.reset()
        gold.reset()
        hero.update()
        cyborg.update()
        w1.draw_wall()  
        if sprite.collide_rect(hero, cyborg):
            finish = True
            window.blit(lose, (200, 200))

    for e in event.get():
        if e.type == QUIT:
            game = False  
    display.update()
    clock.tick(60)
from pygame import *