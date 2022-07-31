from math   import cos, sin
from random import randint, choice
import pygame

DeltaTime = 1



class ParticleCircle :
	def __init__ (self, pos, dir_, vel, color, size, life, gravity) :
		self.posX, self.posY = pos[0], pos[1]
		self.size  = size
		self.angle = dir_
		self.vel   = vel
		self.color = color
		self.max_life = life
		self.life  = life
		self.g = gravity
		self.velY = 0


	def update (self) :
		self.velY += self.g
		self.posX += cos(self.angle) * self.vel
		self.posY += (sin(self.angle) * self.vel) + self.velY
		self.life -= 1


	def draw (self, root) : pygame.draw.circle(root, self.color, (self.posX, self.posY), ((self.size/self.max_life)*self.life))



class ParticlePulse :
	def __init__ (self, pos, thickness, color, size, life) :
		self.posX, self.posY = pos[0], pos[1]
		self.size     = size
		self.max_size = size
		self.color = color
		self.life  = life
		self.thickness = thickness
		self.max_thickness = thickness
		#60 / 5 = 12


	def update (self) :
		self.life -= 1
		self.size *= 0.8


	def draw (self, root) :
		a = round(((self.life/4)/self.max_thickness)*self.thickness)
		if a <= 0 : a = 1
		pygame.draw.circle(root, self.color, (self.posX, self.posY), self.max_size-self.size, width=a)



class ParticleSparcle :
	def __init__ (self, pos, color, life, angle, velocity) :
		self.posX, self.posY = pos[0], pos[1]
		self.vel   = velocity
		self.angle = angle
		self.color = color
		self.life  = life


	def update(self) :
		self.life -= 1
		self.posX += cos(self.angle) * self.vel
		self.posY += sin(self.angle) * self.vel


	def draw (self, root) :
		pygame.draw.polygon(root, self.color, [
			((self.posX - (cos(self.angle) * self.vel * 4)), (self.posY - (sin(self.angle) * self.vel * 4))),
			((self.posX - (sin(self.angle) * 3)), (self.posY - (cos(self.angle) * 3))),
			((self.posX + (cos(self.angle) * self.vel * 1.25)), (self.posY + (sin(self.angle) * self.vel * 1.25))),
			((self.posX + (sin(self.angle) * 3)), (self.posY + (cos(self.angle) * 3)))])


"""
class ParticleExplosion :
	def __init__ (self, pos, size, life):
		self.posX, self.posY = pos[0], pos[1]
		self.life, self.anim = life, 0
		self.size = size
		# yellow orange bown red circles generation
		self.stages = []
		a = []
		for i in range(30) :
			if randint(0, 1) : x = self.posX+randint(10, round(self.size/3))
			else : x = self.posX-randint(10, round(self.size/2))
			if randint(0, 1) : y = self.posY+randint(10, round(self.size/3))
			else : y = self.posY-randint(10, round(self.size/2))
			distance = abs(self.posX-x) + abs(self.posY-y)
			a.append([
				choice([(255, 255, 0), (255, 200, 0), (255, 150, 0), (255, 100, 0), (100, 40, 20)]),
				(x, y),
				(self.size-distance)/6])
		self.stages.append(a)
		b = []
		for i in range(30) :
			if randint(0, 1) : x = self.posX+randint(10, round(self.size/3))
			else : x = self.posX-randint(10, round(self.size/2))
			if randint(0, 1) : y = self.posY+randint(10, round(self.size/3))
			else : y = self.posY-randint(10, round(self.size/2))
			distance = abs(self.posX-x) + abs(self.posY-y)
			b.append([
				choice([(255, 255, 0), (255, 200, 0), (255, 150, 0), (255, 100, 0), (100, 40, 20)]),
				(x, y),
				(self.size-distance)/2])
		self.stages.append(b)
		##############
		self.particles = [
			ParticleMeeleSwipe((self.posX, self.posY), (255, 255, 255), 20, randint(0, 60)/10, 130),
			ParticlePulse((self.posX, self.posY), 3, (255, 255, 255), 150, 20)]


	def update (self) :
		self.life -= 1
		self.anim += 1
		for particle in self.particles: particle.update()


	def draw (self, root) :
		for particle in self.particles: particle.draw(root)
		if self.anim > 0  and self.anim < 2 : pygame.draw.circle(root, (255, 255, 255), (self.posX, self.posY), 50)
		if self.anim > 2  and self.anim < 7 : pygame.draw.circle(root, (0, 0, 0), (self.posX, self.posY), 5)
		if self.anim > 7  and self.anim < 10 : pygame.draw.circle(root, (255, 255, 255), (self.posX, self.posY), 75)
		if self.anim > 10 and self.anim < 15 :
			for circle in self.stages[0] : pygame.draw.circle(root, circle[0], circle[1], circle[2])
		if self.anim > 15 and self.anim < 22 :
			for circle in self.stages[1] : pygame.draw.circle(root, circle[0], circle[1], circle[2])
"""


class ParticleMeeleSwipe :
	def __init__ (self, pos, color, life, angle, length) :
		self.posX, self.posY = pos[0], pos[1]
		self.angle = angle
		self.color = color
		self.life  = life
		self.length = length


	def update (self) : self.life -=  1


	def draw (self, root) :
		pygame.draw.polygon(root, self.color, [
			((self.posX - (cos(self.angle) * (10+self.length))), (self.posY - (sin(self.angle) * (10+self.length)))),
			((self.posX - (sin(self.angle) * 3)), (self.posY - (cos(self.angle) * 3))),
			((self.posX + (cos(self.angle) * (10+self.length))), (self.posY + (sin(self.angle) * (10+self.length)))),
			((self.posX + (sin(self.angle) * 3)), (self.posY + (cos(self.angle) * 3)))])

#################################################

class ParticleSourceCircle :
	def __init__ (self, pos, color, direction, velocity, size, life, wait, gravity) :
		# initial values and type of particles
		self.posX, self.posY = pos[0], pos[1]
		self.color = color
		self.dir   = direction
		self.vel   = velocity
		self.size  = size
		self.life  = life
		self.max_wait = wait
		self.wait     = wait
		self.g = gravity
		# particles array whitch belong to this source 
		self.particles = []


	def update (self) :
		# updating particles
		for particle in self.particles :
			if particle.life > 0 : particle.update()
			else : self.particles.remove(particle)
		# add more particles
		if self.wait == 0 :
			self.particles.append(ParticleCircle(
				(self.posX, self.posY),
				(randint(self.dir[0]*10-self.dir[1]*10, self.dir[0]*10+self.dir[1]*10)/10),
				randint(self.vel[0]-self.vel[1], self.vel[0]+self.vel[1]),
				self.color,
				randint(self.size[0]-self.size[1], self.size[0]+self.size[1]),
				self.life,
				self.g))
			self.wait = self.max_wait
		else : self.wait -= 1

	def draw (self, root) :
		for particle in self.particles : particle.draw(root)



class ParticleSourcePulse :
	def __init__ (self, pos, color, size, thickness, life, wait) :
		# initial values and type of particles
		self.posX, self.posY = pos[0], pos[1]
		self.color = color
		self.size  = size
		self.life  = life
		self.thickness = thickness
		self.max_wait = wait
		self.wait     = wait
		# particles array whitch belong to this source 
		self.particles = []


	def update (self) :
		# updating particles
		for particle in self.particles :
			if particle.life > 0 : particle.update()
			else : self.particles.remove(particle)
		# add more particles
		if self.wait == 0 :
			self.particles.append(ParticlePulse(
				(self.posX, self.posY),
				self.thickness,
				self.color,
				randint(self.size[0]-self.size[1], self.size[0]+self.size[1]),
				self.life))
			self.wait = self.max_wait
		else : self.wait -= 1


	def draw (self, root) :
		for particle in self.particles : particle.draw(root)



class ParticleSourceSparcle :
	def __init__ (self, pos, color, life, wait, velocity) :
		# initial values and type of particles
		self.posX, self.posY = pos[0], pos[1]
		self.vel   = velocity
		self.color = color
		self.life  = life
		self.wait  = wait
		self.max_wait = wait
		# particles array whitch belong to this source 
		self.particles = []


	def update (self) :
		# updating particles
		for particle in self.particles :
			if particle.life > 0 : particle.update()
			else : self.particles.remove(particle)
		# add more particles
		if self.wait == 0 :
			#  pos, color, life, angle, velocity
			self.particles.append(ParticleSparcle(
				(self.posX, self.posY),
				self.color,
				self.life,
				randint(0, 60)/10,
				self.vel))
			self.wait = self.max_wait
		else : self.wait -= 1


	def draw (self, root) :
		for particle in self.particles : particle.draw(root)


"""
class ParticleSourceExplosion :
	def __init__ (self, pos, wait, life, size):
		self.posX, self.posY = pos[0], pos[1]
		self.wait, self.max_wait = wait, wait
		self.size = size
		self.particles = []
		self.life = life


	def update (self) :
		# updating particles
		for particle in self.particles :
			if particle.life > 0 : particle.update()
			else : self.particles.remove(particle)
		# add more particles
		if self.wait == 0 :
			#  pos, color, life, angle, velocity
			self.particles.append(ParticleExplosion(
				(self.posX, self.posY),
				randint((self.size[0]-self.size[1]), (self.size[0]+self.size[1])),
				self.life))
			self.wait = self.max_wait
		else : self.wait -= 1


	def draw (self, root) :
		for particle in self.particles : particle.draw(root)
"""


class ParticleSourceMeeleSwipe :
	def __init__ (self, pos, color, length, life, wait) :
		# initial values and type of particles
		self.posX, self.posY = pos[0], pos[1]
		self.color = color
		self.life  = life
		self.lenght = length
		self.max_wait = wait
		self.wait     = wait
		# particles array whitch belong to this source 
		self.particles = []


	def update (self) :
		# updating particles
		for particle in self.particles :
			if particle.life > 0 : particle.update()
			else : self.particles.remove(particle)
		# add more particles
		if self.wait == 0 :
			self.particles.append(ParticleMeeleSwipe(
				(self.posX, self.posY),
				self.color,
				self.life,
				randint(0, 60)/10,
				self.lenght))
			self.wait = self.max_wait
		else : self.wait -= 1


	def draw (self, root) :
		for particle in self.particles : particle.draw(root)



print("PyParticles: Hight amount of particles (+8000) may cause lag.")