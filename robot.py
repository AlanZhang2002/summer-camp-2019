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

	def autonomousPeriodic(self):
		"""This function is called periodically during autonomous."""

	def teleopInit(self):
		"""This function is run once each time the robot enters the teleoperated mode."""

	def teleopPeriodic(self):
		"""This function is called periodically during operator control."""
		self.leftSparks.set(-self.joystick1.getY() + self.joystick2.getX())
		self.rightSparks.set(self.joystick1.getY() + self.joystick2.getX())

	def disabledInit(self):
		"""This function is run once each time the robot enters the disabled mode."""

	def disabledPeriodic(self):
		"""This function is called periodically during disabled."""


if __name__ == "__main__":
	wpilib.run(MyRobot)
