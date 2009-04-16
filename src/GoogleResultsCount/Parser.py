import Config

import sgmllib,re
		
class Parser(sgmllib.SGMLParser):
	"A simple parser class - get the Results Count from a Google Search."


	def parse(self, s):
		"Parse the given string 's'."

		# we will stop while processing - in case the results 
		# have been found - and have to take care of that... 
		try:
			self.feed(s)
		except IndexError:
			pass

		self.close()


	def start_table(self, attribute):
		"Process the start of a table."
		
		pass


	def end_table(self):
		"Process the end of a table."

		if re.compile(Config.resultsMatcher).search(self.textContent):
			self.resultsLine = self.textContent

			# this will raise an exception...
			self.reset()

		self.textContent = ''


	def handle_data(self, data):
		"Handle textual 'data'."

		self.textContent += data.strip() + ' '
	

	def get_googleResultsCount(self):
		"Return the googleResultsCount."

		resultsCount = re.sub(Config.resultsSubPattern,Config.resultsSubRepl,self.resultsLine)
		resultsCount = re.sub(r'[,.]','',resultsCount)
		if resultsCount == '': resultsCount = '0'
		return resultsCount


	def get_resultsLine(self):
		"Return a list of textual content."

		return self.resultsLine


	def __init__(self, verbose=0):
		"Initialise an object, passing 'verbose' to the superclass."

		sgmllib.SGMLParser.__init__(self, verbose)
		self.resultsCount = 0 
		self.resultsLine = ''
		self.textContent = '' 
