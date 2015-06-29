"""
This is a simple Python program that creates an indexing of an entire website given by the input URL
by following it's anchor tags.

It uses BFS and saves indexed data in JSON

"""

import requests
import Queue
from sys import argv
from timeout import timeout

from parser import *
import json
import visualize



class Crawler(object):
	base = ""	# The base URL
	def __init__(self, arg):
		self.base = str(arg)
		self.index = []
		self.depth = {}
		self.predecessor = {}
		self.savefile = ""

	@timeout(3)	# Don't wait for more than 3 seconds for the webpage to load
	def open(self, URL = None):	# Open the input URL by making a GET request to the server
		try:
			if URL:
				r = requests.get(URL)
			else:
				r = requests.get(self.base)
			return r.content
		except:
			print "Unable to Open URL - " + URL

# A simple crawl function based on breadth first search and limited by maxdepth
# and by the maximum number of pages that can be indexed

	def Crawl(self, maxdepth = 5, maxpages = 100, only_sublinks = False):

		q = Queue.Queue()
		q.put(self.base)
		self.depth[self.base] = 0
		currURL = ""
		links = list()
		added = list()
		added.append(self.base)

		while ((not q.empty()) and (len(self.predecessor) < maxpages)): # Crawling a maximum of maxpages
			currURL = q.get()
			
			#print currURL
			self.index.append(currURL)
			if (self.depth[currURL] > maxdepth):	# Don't crawl more than the maxdepth
			 	break

			links = self.get_links(currURL, only_sublinks)
			for curr_link in links:
				if curr_link not in added:
					q.put(curr_link)
					added.append(curr_link)
					self.predecessor[curr_link] = currURL
					self.depth[curr_link] = 1 + self.depth[currURL]

			#print "New Page"

# A function that returns a list of all hyperlinks on the input URL

	def get_links(self, URL, only_sublinks):
		html = self.open(URL)	# Open the input URL
		p = Parser(html)
		if not only_sublinks:
			p.find_href(self.base)
			return p.allhref
		else:
			p.find_subhref(self.base)
			return p.sublinks
				

	def save_URLS(self):
		try:
			file_name = (self.base).replace('://', '')
			with open("data/%s_index.json" % file_name, 'w') as fp:
				json.dump(self.index, fp)
			
			with open("data/%s_pred.json" % file_name, 'w') as fp:
				json.dump(self.predecessor, fp)

			with open("data/%s_depth.json" % file_name, 'w') as fp:
				json.dump(self.depth, fp)
			
			self.savefile = file_name
		
		except:
			print "Unable to save URL"


	def plot(self):
		try:
			visualize.plot_network(self.savefile)
		
		except:
			print "Graph Plotting Error"



