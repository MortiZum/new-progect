#Создай собственный Шутер!

from typing import Any
from pygame import *
from random import *

score = 0


clock = time.Clock()
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
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx,
        self.rect.centery, 5)
        bullets.add(bullet)


class Enemy(GameSprite):
    direction = 'right'
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = 0



class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()


rocket = Player('rocket.png', 300, 400, 3)
ufo = Enemy('ufo.png', 400, 400, 5)
import pygame

pygame.init()

window = display.set_mode((700, 500))
display.set_caption('Шутер')
galaxy = transform.scale(image.load('galaxy.jpg'), (800, 600))

pygame.display.set_caption("Шутер")

bullets = sprite.Group()
monsters = sprite.Group()
for i in range(5):
    monster = Enemy('ufo.png', randint(0, 650),
    randint(-200, -50), randint(1, 5))
    monsters.add(monster)

bullets = sprite.Group()


while True:
    window.blit(galaxy, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                rocket.fire()
        
    rocket.reset()
    rocket.update()
    monsters.update()
    monsters.draw(window)
    bullets.update()
    bullets.draw(window)
    collides = sprite.groupcollide(monsters, 
    bullets, True, True)
    for c in collides:
        score += 1
        monster = Enemy('ufo.png', randint(0, 650),
    randint(-200, -50), randint(1, 5))
        monsters.add(monster)

    pygame.display.update()
    clock.tick(60)
    

