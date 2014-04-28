class KillData():
	# link
	# name
	# amount
	# date "yyyy-mm-dd hh:mm:ss"
	# Ship type

	@property
	def link(self):
	    return self._link
	@link.setter
	def link(self, value):
	    self._link = value
	
	@property
	def amount(self):
	    return self._amount
	@amount.setter
	def amount(self, value):
	    self._amount = value

	@property
	def date(self):
	    return self._date
	@date.setter
	def date(self, value):
	    self._date = value
	
	@property
	def name(self):
	    return self._name
	@name.setter
	def name(self, value):
	    self._name = value

	@property
	def shipType(self):
	    return self._shipType
	@shipType.setter
	def shipType(self, value):
	    self._shipType = mapShipType(value)

	def __mapShipType__(imageName):
		return "Frieghter"
	