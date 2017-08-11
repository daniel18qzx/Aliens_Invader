import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))  #set a game display window
	pygame.display.set_caption("Alien Invasion")
	alien=Alien(ai_settings,screen)

# Make a ship.
	ship=Ship(ai_settings,screen)
	bullets=Group()
	aliens=Group()

	gf.create_fleet(ai_settings,screen,ship,aliens)

	while True:  #Main game loop
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()