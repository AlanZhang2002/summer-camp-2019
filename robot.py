import wpilib
import rev
import math
from networktables import NetworkTables

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

		self.openCloseSolenoid = wpilib.DoubleSolenoid(2, 5)
		self.inOutSolenoid = wpilib.DoubleSolenoid(3, 4)

		self.limelight = NetworkTables.getTable("limelight")

	def autonomousInit(self):
		"""This function is run once each time the robot enters the autonomous mode."""
		self.target = 60 #inches
		self.leftSpark1.getEncoder().setPosition(0)
		self.leftSpark1.getEncoder().setPositionConversionFactor(18 * math.pi / 23) #copied from DrivetrainConstants in 2019-Private


	def autonomousPeriodic(self):
		rotations = 0 #self.leftSpark1.getEncoder().getPosition() #assertionerror for some reason
		"""This function is called periodically during autonomous."""
		if self.target < rotations:
			self.leftSparks.set(0.35) #check if it moves forwards pls thank
			self.rightSparks.set(-0.35)
		elif self.target > rotations:
			self.leftSparks.set(-0.35)
			self.rightSparks.set(0.35)


	def teleopInit(self):
		"""This function is run once each time the robot enters the teleoperated mode."""

	def teleopPeriodic(self):
		"""This function is called periodically during operator control."""
		# self.leftSparks.set(-(self.joystick1.getY() - self.joystick2.getY())) commented out for vision
		# self.rightSparks.set(self.joystick1.getY() + self.joystick2.getY())

		if self.joystick1.getTrigger == True:
			self.openCloseSolenoid.set(2)
		else:
			self.openCloseSolenoid.set(1)

		if self.joystick2.getTrigger == True:
			self.inOutSolenoid.set(1)
		else:
			self.inOutSolenoid.set(2)

		self.numTarget = self.limelight.getNumber('tv', 0)
		self.targetOffsetX = self.limelight.getNumber('tx', 0)

		if self.numTarget : #idek if i did this right
			if self.targetOffsetX < -0.5:
				self.leftSparks.set(-(self.joystick1.getY + 0.5))
				self.rightSparks.set(self.joystick1.getY - 0.5)
			elif self.targetOffsetX > 0.5:
				self.leftSparks.set(-(self.joystick1.getY - 0.5))
				self.rightSparks.set(self.joystick1.getY + 0.5)

	def disabledInit(self):
		"""This function is run once each time the robot enters the disabled mode."""

	def disabledPeriodic(self):
		"""This function is called periodically during disabled."""


if __name__ == "__main__":
	wpilib.run(MyRobot)