import Config
import urllib

class URLOpener(urllib.FancyURLopener):
	"use a special 'browser tag' when making the connect"
	
	version = Config.browserTag 
