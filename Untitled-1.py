from pygame import *
import random 


class GameSprite(sprite.Sprite):
    def __init__(self, player_x, player_y, player_speed, player_image, sprite_height, sprite_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sprite_width, sprite_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_x, player_y, player_speed, player_image, sprite_height, sprite_width):
        super().__init__(player_x, player_y, player_speed, player_image, sprite_height, sprite_width)
    def update(left):
        key_click = key.get_pressed()
        if key_click[K_w]:
            self.rect.y -= self.speed
        if key_click[K_s]:
            self.rect.y += self.speed
    def update(right)
        if key_click[K_UP]:
            self.rect.y -= self.speed
        if key_click[K_DOWN]:
            self.rect.y -= self.speed