import wpilib
import rev

class MyRobot(wpilib.IterativeRobot):
	def robotInit(self):
		"""
		This function is called upon program startup and
		should be used for any initialization code.
		"""
		self.leftSpark1 = rev.CANSparkMax(15, rev.MotorType.kBrushless)
		self.leftSpark2 = rev.CANSparkMax(14, rev.MotorType.kBrushless)
		self.leftSpark3 = rev.CANSparkMax(13, rev.MotorType.kBrushless)
		self.rightSpark1 = rev.CANSparkMax(20, rev.MotorType.kBrushless)
		self.rightSpark2 = rev.CANSparkMax(1, rev.MotorType.kBrushless)
		self.rightSpark3 = rev.CANSparkMax(2, rev.MotorType.kBrushless)

		self.joystick1 = wpilib.Joystick(0)
		self.joystick2 = wpilib.Joystick(1)

		self.leftSparks = wpilib.SpeedControllerGroup(self.leftSpark1, self.leftSpark2, self.leftSpark3)
		self.rightSparks = wpilib.SpeedControllerGroup(self.rightSpark1, self.rightSpark2, self.rightSpark3)

	def autonomousInit(self):
		"""This function is run once each time the robot enters the autonomous mode."""
		self.timer = 0

	def autonomousPeriodic(self):
		"""This function is called periodically during autonomous."""
		self.timer += 1
		if self.timer < 150:
			self.leftSparks.set(0.5)
			self.rightSparks.set(-0.5)
		else:
			self.leftSparks.set(0)
			self.rightSparks.set(0)

	def teleopInit(self):
		"""This function is run once each time the robot enters the teleoperated mode."""

	def teleopPeriodic(self):
		"""This function is called periodically during operator control."""
		self.leftSparks.set(self.joystick1.getY() - self.joystick2.getY())
		self.rightSparks.set(-(self.joystick1.getY() + self.joystick2.getY())) #someone check this, idk if it is right

	def disabledInit(self):
		"""This function is run once each time the robot enters the disabled mode."""

	def disabledPeriodic(self):
		"""This function is called periodically during disabled."""


if __name__ == "__main__":
	wpilib.run(MyRobot)
