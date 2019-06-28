import wpilib

class MyRobot(wpilib.TimedRobot):
	
	# Runs once at the beginning, when the robot is turned on
	def robotInit(self):
		return


	# Runs once at the beginning of teleop mode
	def teleopInit(self):
		return


	# Runs repeatedly every 20ms in teleop mode
	def teleopPeriodic(self):
		return


	# Runs once at the beginning of autonomous mode
	def autonomousInit(self):
		return


	# Runs repeatedly every 20ms in autonomous mode
	def autonomousPeriodic(self):
		return


	# Runs once at the beginning when disabled
	def disabledInit(self):
		return


	# Runs repeatedly every 20ms while the robot is disabled
	def disabledPeriodic(self):
		# leave blank?
		return

if __name__ == "__main__":
	wpilib.run(MyRobot)