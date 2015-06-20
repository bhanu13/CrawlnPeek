# A simple Parser class that finds all hyperlinks and src files in a html file
# Has 2 lists that contain all href and src file links

class Parser(object):
 	allhref = []
 	allsrc = []
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

	def find_src(self):
		position = 0
		while True:
			if self.data:
				position = self.data.find("src", position)
				if (position == -1):
					break
				else:
					start_q = self.data.find('"', position)
					end_q = self.data.find('"', start_q + 1)
					url = self.data[start_q+1:end_q]
					if(url[0:4] == "http"):
						self.allsrc.append(url)
					position = end_q
			else:
				break

# p = Parser(code)
# p.find_href()
# print p.allhref

