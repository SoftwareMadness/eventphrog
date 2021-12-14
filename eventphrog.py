from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class EventPhrog:
	def create_driver(self):
		options = Options()
		options.headless = True
		self.driver = webdriver.Firefox(options=options)

	def open_event(self,url):
		self.driver.get(url)
		self.lSeatMapData = self.driver.execute_script("return lSeatMapData;")

	def getTicket(self,ticketid):
		return self.driver.execute_script("return MobileSaalplaner.getTicket("+str(ticketid)+");")

	def getSeatMapData(self):
		return self.lSeatMapData

	def getSeats(self):
		return self.lSeatMapData["seats"]

	def resolveAllSeatTickets(self):
		i = 50
		st = []
		for seatmap in self.lSeatMapData["seats"]:
			st.append(self.getTicket(seatmap["ticketId"]))
			if i == 0:
				break
			i -= 1
		return st
		
	def getFreeSeats(self):
		free = []
		for ticket in self.resolveAllSeatTickets():
			if not ticket["reservedByUser"]:
				free.append(ticket)
		return free
		
	def getRatio(self):
		return (len(self.getFreeSeats()),len(self.resolveAllSeatTickets()))
		
	def close(self):
		self.driver.close()
	
