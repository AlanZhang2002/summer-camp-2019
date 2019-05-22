import wpilib
import ctre.WPI_TalonSRX

class MyRobot(wpilib.TimedRobot):


	# Runs once at the beginning, when the robot is turned on
	def robotInit(self):
		"""initialize robot parts here"""
		self.talon = ctre.WPI_TalonSRX(1)
		self.joystick = wpilib.Joystick(0)


	# Runs once at the beginning of teleop mode
	def teleopInit(self):



	# Runs repeatedly every 20ms in teleop mode
	def teleopPeriodic(self):



	# Runs once at the beginning of autonomous mode
	def autonomousInit(self):



	# Runs repeatedly every 20ms in autonomous mode
	def autonomousPeriodic(self):



	# Runs once at the beginning when disabled
	def disabledInit(self):



	# Runs repeatedly every 20ms while the robot is disabled
	def disabledPeriodic(self):
		# leave blank?
