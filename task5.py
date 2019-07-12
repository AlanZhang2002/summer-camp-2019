import wpilib
import rev
import math

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

		self.leftSpark1.setIdleMode(rev.IdleMode.kBrake)
		self.leftSpark2.setIdleMode(rev.IdleMode.kBrake)
		self.leftSpark3.setIdleMode(rev.IdleMode.kBrake)
		self.rightSpark1.setIdleMode(rev.IdleMode.kBrake)
		self.rightSpark2.setIdleMode(rev.IdleMode.kBrake)
		self.rightSpark3.setIdleMode(rev.IdleMode.kBrake)

		self.openCloseSolenoid = wpilib.DoubleSolenoid(2, 5)
		self.inOutSolenoid = wpilib.DoubleSolenoid(3, 4)

	def autonomousInit(self):
		"""This function is run once each time the robot enters the autonomous mode."""
		self.target = 60 #inches
		self.leftSpark1.getEncoder().setPosition(0.0)
		self.leftSpark1.getEncoder().setPositionConversionFactor(18 * math.pi / 23)
		self.allowable_error = 1
		self.in_zone_count = 0
		self.in_zone_threshold = 15
		self.should_stop = False

	def autonomousPeriodic(self):
		rotations = self.leftSpark1.getEncoder().getPosition()
		"""This function is called periodically during autonomous."""
		if (abs(self.target - rotations) < self.allowable_error):
			self.in_zone_count += 1
		else:
			self.in_zone_count = 0

		if (self.in_zone_count < self.in_zone_threshold and not self.should_stop):
			if self.target < rotations:
				self.leftSparks.set(-0.1)
				self.rightSparks.set(0.1)
			elif self.target > rotations:
				self.leftSparks.set(0.1)
				self.rightSparks.set(-0.1)
		else:
			self.leftSparks.set(0)
			self.rightSparks.set(0)
			self.should_stop = True



	def teleopInit(self):
		"""This function is run once each time the robot enters the teleoperated mode."""

	def teleopPeriodic(self):
		"""This function is called periodically during operator control."""
		self.leftSparks.set(-(self.joystick1.getY() - self.joystick2.getY()))
		self.rightSparks.set(self.joystick1.getY() + self.joystick2.getY())

		if self.joystick1.getTrigger():
			self.openCloseSolenoid.set(2)
		else:
			self.openCloseSolenoid.set(1)

		if self.joystick2.getTrigger():
			self.inOutSolenoid.set(1)
		else:
			self.inOutSolenoid.set(2)

	def disabledInit(self):
		"""This function is run once each time the robot enters the disabled mode."""

	def disabledPeriodic(self):
		"""This function is called periodically during disabled."""


if __name__ == "__main__":
	wpilib.run(MyRobot)