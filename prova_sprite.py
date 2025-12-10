import arcade
import os
# from arcade import *

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.sprite = None
        self.playerSpriteList = arcade.SpriteList()
        self.keys_pressed = {
            'up': False,
            'down': False,
            'left': False,
            'right': False
        }

        self.setup()

    def setup(self):
        
        self.sprite = arcade.Sprite("./asset/2D Pixel Dungeon Asset Pack v2.0/2D Pixel Dungeon Asset Pack/Character_animation/priests_idle/priest2/v1/priest2_v1_1.png")

        self.sprite.center_x = 100
        self.sprite.center_y = 100
        self.sprite.scale_x = 5.0
        self.sprite.scale_y = 5.0
        self.speed=100
        self.velocity_x = 0
        self.velocity_y = 0

        self.playerSpriteList.append(self.sprite)

    def on_draw(self):
        self.clear()
        self.playerSpriteList.draw()

    def update_velocity(self):
        """Aggiorna la velocità in base ai tasti premuti"""
        self.velocity_x = 0
        self.velocity_y = 0

        if self.keys_pressed['up']:
            self.velocity_y = self.speed
        if self.keys_pressed['down']:
            self.velocity_y = -self.speed
        if self.keys_pressed['left']:
            self.velocity_x = -self.speed
        if self.keys_pressed['right']:
            self.velocity_x = self.speed
        
    def on_update(self, deltaTime):
        self.sprite.center_x += self.velocity_x * deltaTime
        self.sprite.center_y += self.velocity_y * deltaTime

    def on_key_press(self, key, modifiers):
        """Gestisce la pressione dei tasti"""
        if key in [arcade.key.UP, arcade.key.W]:
            self.keys_pressed['up'] = True
        elif key in [arcade.key.DOWN, arcade.key.S]:
            self.keys_pressed['down'] = True
        elif key in [arcade.key.LEFT, arcade.key.A]:
            self.keys_pressed['left'] = True
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.keys_pressed['right'] = True

        self.update_velocity()
    
    
    def on_key_release(self, key, modifiers):
        """Gestisce il rilascio dei tasti"""
        if key in [arcade.key.UP, arcade.key.W]:
            self.keys_pressed['up'] = False
        elif key in [arcade.key.DOWN, arcade.key.S]:
            self.keys_pressed['down'] = False
        elif key in [arcade.key.LEFT, arcade.key.A]:
            self.keys_pressed['left'] = False
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.keys_pressed['right'] = False
        
        self.update_velocity()
        




def main():
    game = MyGame(
        600, 600, "Il mio giochino"
    )
    arcade.run()


if __name__ == "__main__":
    main()
