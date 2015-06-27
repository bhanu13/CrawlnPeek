"""
Visualizing the Website Graph generated from indexing.

- Use NetworkX and Matplotlib to create a plot of the website graph
"""
import json

filename = ""	# Name of json file to be opened
with open(filename) as data_file:    
    data = json.load(data_file)

