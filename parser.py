# A simple Parser class that finds all hyperlinks in a html file
# Has a lists that contains all href links

# Add a list of links only in the parent domain.

class Parser(object):
 	allhref = []
 	sublinks = []

 	def __init__(self, data = None):
 		self.data = data

	def find_href(self, base):
		position = 0
		while True:
			if self.data:
				position = self.data.find("<a href", position)
				if (position == -1):
					break
				else:
					start_q = self.data.find('"', position)
					end_q = self.data.find('"', start_q + 1)
					link = self.data[start_q+1:end_q]
					# if(url[0:4] == "http"):
					if link not in self.allhref:
						self.allhref.append(link)
					# Filter the appropriate URLs
					position = end_q
			else:
				break

		for i in range(0, len(self.allhref)):
			if ("http" or "https") not in self.allhref[i]:
				self.allhref[i] = base + self.allhref[i]


	def find_subhref(self, base):
		# if not self.allhref:
		self.find_href(base)

		# Check for different cases - relative links, https: - but then wrt to base
		for link in self.allhref:
			if base in link:
				self.sublinks.append(link)

	# def only_html(self, text):

# p = Parser(code)
# p.find_href()
# print p.allhref

