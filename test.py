from pyparticles import *


class Game :
	def __init__ (self, size, title, fps) :
		#################################
		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption(title)
		#################################
		self.clock = pygame.time.Clock()
		self.FPS = fps


	def update (self) :
		pulse.update()
		spay .update()
		sparcle.update()
		swipe.update()
		g_spay.update()
		


	def render (self) :
		self.screen.fill((10, 10, 10))
		########################
		pulse.draw(self.screen)
		spay .draw(self.screen)
		sparcle.draw(self.screen)
		swipe.draw(self.screen)
		g_spay.draw(self.screen)
		########################
		pygame.display.flip()
		self.clock.tick(self.FPS)


	def start (self) :
		self.running = True
		while self.running :
			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					self.running = False
			self.update()
			self.render()



if __name__ == "__main__":
	############### particles ###################
	spay    = ParticleSourceCircle(
		pos=(50, 125),         # center of sourse of particles
		color=(255, 255, 255), # color of particles
		direction=(0, 0.4),    # direction of particles and it's offset
		velocity=(3, 2),       # velocity of oarticles and it's offset
		size=(5, 3),           # start size of particles and it's offset (can become smaller when almost dead)
		life=40,               # when disapears after certain amount of frames
		wait=0,                # how much frames between particle spawning
		gravity=0)             # gravity for particles
	g_spay  = ParticleSourceCircle(
		pos=(375, 375),        # center of sourse of particles
		color=(255, 255, 255), # color of particles
		direction=(-1.5, 0.4), # direction of particles and it's offset
		velocity=(4, 1),       # velocity of oarticles and it's offset
		size=(5, 3),           # start size of particles and it's offset (can become smaller when almost dead)
		life=120,              # when disapears after certain amount of frames
		wait=0,                # how much frames between particle spawning
		gravity=0.1)           # gravity for particles
	pulse   = ParticleSourcePulse(
		pos=(390, 125),        # center of sourse of particles
		color=(255, 255, 255), # color of particles
		size=(100, 10),        # size of particles and it's offset
		thickness=0.1,         # thickness of pulse wave
		life=30,               # when disapears after certain amount of frames
		wait=50)               # how much frames between particle spawning
	sparcle = ParticleSourceSparcle(
		(125, 275),            # center of sourse of particles
		(255, 255, 255),       # color of particles
		20,                    # when disapears after certain amount of frames
		0,                     # how much frames between particle spawning
		3)
	swipe   = ParticleSourceMeeleSwipe(
		(125, 425),            # center of sourse of particles
		(255, 255, 255),       # color of particles
		50,                    # length of  swipe
		20,                    # when disapears after certain amount of frames
		20)                    # how much frames between particle spawning
	######## game ###############################
	game = Game((500, 500), "PyParticle test", 60)
	game.start()