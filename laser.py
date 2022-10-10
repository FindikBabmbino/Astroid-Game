import pygame
class Laser(pygame.sprite.Sprite):
	def __init__(self,group,pos):
		super().__init__(group)
		self.image=pygame.image.load("graphics/laser.png").convert_alpha()
		self.rect=self.image.get_rect(midbottom=pos)

		#float based position
		self.pos=pygame.math.Vector2(self.rect.topleft)
		self.direction=pygame.math.Vector2(0,-1)
		self.speed=600

		#mask
		self.mask=pygame.mask.from_surface(self.image)

		#sound
		self.explode_sound=pygame.mixer.Sound("sounds/explosion.wav")


	def meteor_collision(self,meteor_group):
		if pygame.sprite.spritecollide(self,meteor_group,True,pygame.sprite.collide_mask):
			self.explode_sound.play()
			self.kill()

	def update(self,delta_time,meteor_group):
		self.pos+=self.direction*self.speed*delta_time
		self.rect.topleft=(round(self.pos.x),round(self.pos.y))
		self.meteor_collision(meteor_group)

		if self.rect.bottom<0:
			self.kill()
