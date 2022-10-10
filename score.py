import pygame
class Score:
	def __init__(self):
		self.font=pygame.font.Font("graphics/subatomic.ttf",50)

	def display(self,display_surf,width,height):
		score_text=(f"Score:{pygame.time.get_ticks()//1000}")
		text_surf=self.font.render(score_text,True,"White")
		text_rect=text_surf.get_rect(midbottom=(width/2,height-80))
		display_surf.blit(text_surf,text_rect)
		pygame.draw.rect(display_surf,"white",text_rect.inflate(30,30),width=8,border_radius=5)