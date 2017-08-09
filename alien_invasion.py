import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))  #set a game display window
	pygame.display.set_caption("Alien Invasion")

# Make a ship.
	ship=Ship(ai_settings,screen)
	bullets=Group()

	while True:  #Main game loop
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_screen(ai_settings,screen,ship,bullets)

		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		print(len(bullets))

run_game()