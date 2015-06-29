<h2>CrawlnPeek | A Micro WebCrawler and Network Visualizer </h2>
The program <b>crawls</b> the given website URL by following anchor tags based on Breadth First Search and indexes the website.
Then it saves the relevant crawled data in JSON and <b>visualizes</b> the domain's connectivity.

<h3>Usage:</h3>

python main.py <http://www.example.com>

<h3>Features:</h3>
- Creates a list of all pages indexed on a website
- Creates a list of indexed pages with their relative depths and respective predecessors
- Creates an image of the website network
- Saves the indexed URLs to a JSON file
- Added robustness to handle complex data parsing and broken hyperlinks
- Added limits for maxdepth and maxpages indexed
- Added support for relative links i.e. (href = "/source")


<h3>Requirements:</h3>
- <a href = "http://docs.python-requests.org/en/latest/">Requests</a> or Requests[Security] to allow true SSL connections
- <a href = "https://docs.python.org/3/library/json.html">JSON</a> library
- <a href = "http://matplotlib.org/api/pyplot_api.html">Matplotlib</a> to allow plotting the graph
- <a href = "https://networkx.github.io/">Networkx</a> to create the Graph using the list data

<h3>Examples:</h3>
<b>An image of codeacademy.com Network:</b>
<div align = "center"><img src = "data/codecademy.png"></div>
<b>An image of google.com Network @ 100 pages:</b>
<div align = "center"><img src = "data/googlemap.png"></div>

<b>NOTE</b>: Crawling can sometimes a really long time depending on the maxpages specified. It has a default value of 100 pages.

<h3>Future:</h3>
- Set up a web app to perform crawling on a given user query and then present an interactive visualization.
- Use d3.js to visualize the website tree.

Author - bagarwa2
