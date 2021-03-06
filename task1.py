import wpilib
import rev

class MyRobot(wpilib.IterativeRobot):
	def robotInit(self):
		"""
		This function is called upon program startup and
		should be used for any initialization code.
		"""
		self.spark = rev.CANSparkMax(1, rev.MotorType.kBrushless) #(deviceID, type)
		self.joystick = wpilib.Joystick(0)

	def autonomousInit(self):
		"""This function is run once each time the robot enters the autonomous mode."""

	def autonomousPeriodic(self):
		"""This function is called periodically during autonomous."""

	def teleopInit(self):
		"""This function is run once each time the robot enters the teleoperated mode."""

	def teleopPeriodic(self):
		"""This function is called periodically during operator control."""
		self.spark.set(self.joystick.getX())

	def disabledInit(self):
		"""This function is run once each time the robot enters the disabled mode."""

	def disabledPeriodic(self):
		"""This function is called periodically during disabled."""


if __name__ == "__main__":
	wpilib.run(MyRobot)