import pygame,sys
from laser import Laser
class Ship(pygame.sprite.Sprite):
	def __init__(self,groups,pos,laser_group,firerate=500):
		#we have to init parent class
		super().__init__(groups)
		# we need a surface
		self.image=pygame.image.load("graphics/ship.png").convert_alpha()
		self.rect=self.image.get_rect(center=pos)
		self.firerate=firerate
		#timer
		self.can_shoot=True
		self.shoot_time=0

		#laser
		self.laser_group=laser_group

		#mask
		self.mask=pygame.mask.from_surface(self.image)

		#sound
		self.laser_sound=pygame.mixer.Sound("sounds/laser.ogg")

	def input_position(self):
		pos=pygame.mouse.get_pos()
		self.rect.center=pos

	def reset_laser_timer(self):
		if not self.can_shoot:
			current_time=pygame.time.get_ticks()
			if current_time-self.shoot_time>self.firerate:
				self.can_shoot=True

	def laser_shoot(self):
		if pygame.mouse.get_pressed()[0] and self.can_shoot:
			Laser(self.laser_group,self.rect.midtop)
			self.laser_sound.play()
			self.shoot_time=pygame.time.get_ticks()
			self.can_shoot=False

	def meteor_collision(self,meteor_group):
		if pygame.sprite.spritecollide(self,meteor_group,False,pygame.sprite.collide_mask):
			pygame.quit()
			sys.exit()

	def update(self,meteor_group):
		self.reset_laser_timer()
		self.laser_shoot()
		self.input_position()
		self.meteor_collision(meteor_group)