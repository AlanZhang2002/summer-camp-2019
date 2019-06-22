import wpilib
import ctre.WPI_TalonSRX

class MyRobot(wpilib.TimedRobot):


	# Runs once at the beginning, when the robot is turned on
	def robotInit(self):
		"""initialize robot parts here"""
		self.leftTalon1 = ctre.WPI_TalonSRX(15)
		self.leftTalon2 = ctre.WPI_TalonSRX(14)
		self.leftTalon3 = ctre.WPI_TalonSRX(13)
		self.rightTalon1 = ctre.WPI_TalonSRX(20)
		self.rightTalon2 = ctre.WPI_TalonSRX(1)
		self.rightTalon3 = ctre.WPI_TalonSRX(2)

		self.joystick1 = wpilib.Joystick(0)
		self.joystick2 = wpilib.Joystick(1)

		self.leftTalons = wpilib.SpeedControllerGroup(lefttalon1, lefttalon2, lefttalon3)
		self.rightTalons = wpilib.SpeedControllerGroup(righttalon1, righttalon2, righttalon3)


	# Runs once at the beginning of teleop mode
	def teleopInit(self):



	# Runs repeatedly every 20ms in teleop mode
	def teleopPeriodic(self):
		self.leftTalons.set(self.joystick1.getY() - self.joystick2.getY())
		self.rightTalons.set(-(self.joystick1.getY() + self.joystick2.getY())) #someone check this, idk if it is right



	# Runs once at the beginning of autonomous mode
	def autonomousInit(self):
		self.target = 3000
		self.leftTalon1.setSelectedSensorPosition(0, 0, 0)



	# Runs repeatedly every 20ms in autonomous mode
	def autonomousPeriodic(self):
		self.leftTalons.set((self.target - self.leftTalon1.getSelectedSensorPosition(0)) / 3000)
		self.rightTalons.set(-((self.target - self.leftTalon1.getSelectedSensorPosition(0)) / 3000))



	# Runs once at the beginning when disabled
	def disabledInit(self):



	# Runs repeatedly every 20ms while the robot is disabled
	def disabledPeriodic(self):
		# leave blank?
