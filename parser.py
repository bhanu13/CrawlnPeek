# A simple Parser class that finds all hyperlinks in a html file
# Has a lists that contains all href links

class Parser(object):
 	allhref = []

 	def __init__(self, data = None):
 		self.data = data

	def find_href(self):
		position = 0
		while True:
			if self.data:
				position = self.data.find("<a href", position)
				if (position == -1):
					break
				else:
					start_q = self.data.find('"', position)
					end_q = self.data.find('"', start_q + 1)
					url = self.data[start_q+1:end_q]
					if(url[0:4] == "http"):
						self.allhref.append(url)
					position = end_q
			else:
				break


# p = Parser(code)
# p.find_href()
# print p.allhref

