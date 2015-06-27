"""
Visualizing the Website Graph generated from indexing.

- Use NetworkX and Matplotlib to create a plot of the website graph
"""
import json
import networkx as nx
import matplotlib.pyplot as plt

def plot_network(baseURL = None):
	if baseURL:
		G = nx.Graph()
		filename = "data/%s_pred.json" % baseURL	# Name of json file to be opened
		data = openpred(filename)
		for URL in data:
			G.add_edge(URL,data[URL])
		
		nx.draw(G)
		plt.show()
		plt.savefig("data/%s.png" % baseURL)


def openpred(filename = None):
	if filename:
		with open(filename) as data_file:
			data = json.load(data_file)
			return data

# nx.draw_networkx(G)
# nx.draw(G)

# for URL in data:
# 	G.add_node(URL)