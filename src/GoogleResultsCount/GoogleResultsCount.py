import Config, URLOpener, Parser

import sys,os,time
usage = "usage: %s" % os.path.basename(sys.argv[0])

import urllib

# make sure we use urlopen with our parameters
urllib._urlopener = URLOpener.URLOpener(Config.proxies)

for line in open(sys.argv[1]).readlines():

	# get something to work with
	f = urllib.urlopen(Config.searchURL + urllib.quote_plus(line))
	s = f.read()

	# Try and process the page.
	# The class should have been defined first, remember.
	myparser = Parser.Parser()
	myparser.parse(s)

	# Get the googleResultsCount.
	print myparser.get_googleResultsCount() + '\t>' + line.strip()
	sys.stdout.flush()
	
	# wait between requests
	time.sleep(Config.sleep)
