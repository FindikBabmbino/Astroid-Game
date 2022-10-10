import pygame,sys
from ship import Ship
from laser import Laser
from meteor import Meteor
from score import Score

pygame.init()
WINDOW_WIDTH,WINDOW_HEIGHT=1280,720
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock=pygame.time.Clock()

#sprite group there is also GroupSingle which contains only one sprite 
spaceship_group=pygame.sprite.Group()
laser_group=pygame.sprite.Group()
meteor_group=pygame.sprite.Group()

#sprite creation
ship=Ship(spaceship_group,(WINDOW_WIDTH/2,WINDOW_HEIGHT/2),laser_group)
meteor=Meteor(meteor_group)
#laser=Laser(laser_group,ship.rect.midtop)
#spaceship_group.add(ship)

#background
bg_surface=pygame.image.load("graphics/background.png").convert()

#score text
score=Score()

#bg music
bg_music=pygame.mixer.Sound("sounds/music.wav")
bg_music.play(loops=-1)

while True:

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()

	#delta time 
	dt=clock.tick()/1000

	#bg draw
	display_surface.blit(bg_surface,(0,0))
	#score draw
	score.display(display_surface,WINDOW_WIDTH,WINDOW_HEIGHT)

	#update
	spaceship_group.update(meteor_group)
	laser_group.update(dt,meteor_group)
	meteor_group.update(dt)

	#spawn meteor
	if meteor.create_meteor:
		Meteor(meteor_group)

	#draw groups
	spaceship_group.draw(display_surface)
	laser_group.draw(display_surface)
	meteor_group.draw(display_surface)


	#draw the frame
	pygame.display.update()