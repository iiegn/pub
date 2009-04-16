import re

searchURL = 'http://www.google.com/search?q='
# searchURL = 'http://www.google.de/search?hl=en&q='

# ...just a dummy.
searchString = 'blafaselblubber war'

resultsMatcher = re.compile(
	'Web.*Result.*of.*for.*seconds')
resultsSubPattern = re.compile(
	r'.*of(.about)?.([0-9,.]+).for..*')
resultsSubRepl = '\\2'

# this one seems to work...
browserTag = "Links (1.00pre20; Linux 2.6.18-5-686 i686) (Debian pkg 1.00~pre20-0.1)"
# browserTag = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-us) AppleWebKit/523.10.6 (KHTML, like Gecko) Version/3.0.4 Safari/523.10.6"
# browserTag = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"

# ...however, a proxy always increases the chances of getting through with this
proxies = {}
# proxies = {'http': 'http://www-proxy.t-online.de:80'}
# proxies = {'http': 'http://www-proxy.rz.uni-osnabrueck.de:80'}
# proxies = {'http': 'http://proxy:3128'}
#

# how long should we wait between requests?
sleep = 4
