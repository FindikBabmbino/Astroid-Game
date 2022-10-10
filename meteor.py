import pygame
from random import uniform,randint

class Meteor(pygame.sprite.Sprite):

	def __init__(self,groups,min_range_x=-0.5,max_range_x=1):
		self.groups=groups
		super().__init__(self.groups)

		#randomizing the meteor size
		meteor_surf=pygame.image.load("graphics/meteor.png").convert_alpha()
		meteor_size=pygame.math.Vector2(meteor_surf.get_size())*uniform(0.5,1.5)
		self.scaled_surf=pygame.transform.scale(meteor_surf,meteor_size)
		self.image=self.scaled_surf


		self.rect=self.image.get_rect(center=(0,0))

		self.pos=pygame.math.Vector2((randint(-100,1280+100),0))
		self.direction=pygame.math.Vector2(uniform(min_range_x,max_range_x),1)
		self.speed=randint(400,600)

		self.timer=0
		self.create_meteor=True

		#rotation logic
		self.rotation=0
		self.rotation_speed=randint(20,50)

		#mask
		self.mask=pygame.mask.from_surface(self.image)



	def reset_timer(self):
		if not self.create_meteor:
			current_time=pygame.time.get_ticks()
			if current_time-self.timer>500:
				self.create_meteor=True

	def meteor_creation(self,dt):
		if self.create_meteor:
			self.create_meteor=False
			self.timer=pygame.time.get_ticks()

		self.pos+=self.direction*self.speed*dt
		self.rect.bottomleft=(round(self.pos.x),round(self.pos.y))

	def rotate(self,dt):
		self.rotation+=self.rotation_speed*dt
		#rotate_surf=pygame.transform.rotate(self.scaled_surf,self.rotation)
		#this masks the quality loss
		rotate_surf=pygame.transform.rotozoom(self.scaled_surf,self.rotation,1)
		self.image=rotate_surf
		self.rect=self.image.get_rect(center=self.rect.center)
		self.mask=pygame.mask.from_surface(self.image)

	def update(self,dt):
		self.meteor_creation(dt)
		self.reset_timer()
		self.rotate(dt)

