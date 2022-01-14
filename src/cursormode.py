
class Cursormode:
	def __init__(self):
		"""
		Creates an object that allows us to track what the player has selected last
		args: self - Cursormode, object created by the class
		return: self.cursorMode - str, the string that represents what was last selected
		"""
		self.cursorMode = ''

	def modeNull(self):
		"""
		Sets the cursor mode to a "null state", so that nothing is selected
		args: self - Cursormode, object created by the class
		return: self.cursorMode - str, the string that represents what was last selected
		"""
		self.cursorMode = ''
		return self.cursorMode

	def modeSeed(self):
		"""
		Sets the cursor mode to 'SEED' so that the player may plant a seed
		args: self - Cursormode, object created by the class
		return: self.cursorMode - str, the string that represents what was last selected
		"""
		self.cursorMode = 'SEED'
		return self.cursorMode

	def modeWater(self):
		"""
		Sets cursor mode to 'WATER' so that the player can water a plant and let it grow
		args: self - Cursormode, object created by the class
		return: self.cursorMode - str, the string that represents what was last selected
		"""
		self.cursorMode = 'WATER'
		return self.cursorMode

	def modePlant1(self):
		"""
		Sets cursor mode to 'PLANT1' so that the player can select the top left mature plant and sell it
		args: self - Cursormode, object created by the class
		return: self.cursorMode - str, the string that represents what was last selected
		"""
		self.cursorMode = 'PLANT1'
		return self.cursorMode
	
	def modePlant2(self):
		"""
		Sets cursor mode to 'PLANT2' so that the player can select the top right mature plant and sell it
		args: self - Cursormode, object created by the class
		return: self.cursorMode - str, the string that represents what was last selected
		"""
		self.cursorMode = 'PLANT2'
		return self.cursorMode
	
	def modePlant3(self):
		"""
		Sets cursor mode to 'PLANT3' so that the player can select the bottom left mature plant and sell it
		args: self - Cursormode, object created by the class
		return: self.cursorMode - str, the string that represents what was last selected
		"""
		self.cursorMode = 'PLANT3'
		return self.cursorMode
	
	def modePlant4(self):
		"""
		Sets cursor mode to 'PLANT4' so that the player can select the bottom right mature plant and sell it
		args: self - Cursormode, object created by the class
		return: self.cursorMode - str, the string that represents what was last selected
		"""
		self.cursorMode = 'PLANT4'
		return self.cursorMode

