import math

dt = 4
v = 10
omega = math.pi/8


class Robot:
	
	def __init__(self, x0, y0, theta0, t0):
		self.x = x0
		self.y = y0
		self.theta = theta0
		self.t = t0
		
	def progress(self):
		self.x = self.x + v*dt*math.cos(self.theta)
		self.y = self.y + v*dt*math.sin(self.theta)
		self.theta = self.theta + omega*dt
		self.t = self.t + dt
		self.getStatus()
	
	def getStatus(self):
		print 'x = ', self.x
		print 'y = ', self.y
		print 'theta = ', self.theta%(2*math.pi)
		print 't = ', self.t
		print '--------\n'
	
if __name__ == "__main__":
	robot = Robot(0,0,0,0)
	robot.getStatus()
	robot.progress()
	robot.progress()
	robot.progress()
	robot.progress()