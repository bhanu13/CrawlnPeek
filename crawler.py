"""
This is a simple Python program that creates an indexing of an entire website given by the input URL
by following it's anchor tags.
"""

import requests
import Queue
from sys import argv
from timeout import timeout

from parser import *

class Crawler(object):
	"""docstring for ClassName"""
	base = ""
	def __init__(self, arg):
		self.base = str(arg)
		self.index = []
		self.depth = {}
		self.predecessor = {}

	@timeout(3)
	def open(self, URL = None):
		try:
			if URL:
				r = requests.get(URL)
			else:
				r = requests.get(self.base)
			return r.content
		except:
			print "Unable to Open URL"

# A simple crawl function based on breadth first search and limited by maxdepth
# and by the maximum number of pages that can be indexed
	def Crawl(self, maxdepth = 5, maxpages = 100):
		q = Queue.Queue()
		q.put(self.base)
		self.depth[self.base] = 0
		currURL = ""
		links = list()
		added = list()
		added.append(self.base)
		pages = 0
		while (not q.empty() and pages < maxpages): # Crawling a maximum of maxpages
			currURL = q.get()
			pages += 1
			#print currURL
			self.index.append(currURL)
			if (self.depth[currURL] > maxdepth):	# Don't crawl more than the maxdepth
			 	break
			links = self.get_links(currURL)
			for curr_link in links:
				if curr_link not in added:
					q.put(curr_link)
					added.append(curr_link)
					self.predecessor[curr_link] = currURL
					self.depth[curr_link] = 1 + self.depth[currURL]
			#print "New Page"

	def get_links(self, URL):
		html = self.open(URL)
		p = Parser(html)
		p.find_href()
		#parser.anchor_bgn()
		return p.allhref


def main():
	try:
		C = Crawler(str(argv[1]))
		#print C.open()
		#print "Opened the Base page"
		C.Crawl(maxpages = 10)
		#print C.get_links(C.base)
		print C.index
		print C.depth.values()
		print C.predecessor.values()

	except ValueError:	
		print "No URL specified"

	except:
		print "An unexpected error occured"


main()
