A simple Web Crawler in Python.
The program crawls the given website by following anchor tags using Breadth First Search.

Usage:

python main.py <http://www.example.com>

Features:
- Creates a list of all pages indexed on a website
- Creates a list of indexed web pages with their relative depths
- Maps each URL to its parent URL
- Saves the indexed URLs to a JSON file
- Added robustness to handle complex data parsing and broken hyperlinks

Requirements:
- <a href = "http://docs.python-requests.org/en/latest/">Requests</a> or Requests[Security] to allow a true SSL connections

TODO :

Add functionality for parsing links that don't start with http
i.e. Support for relative links (href = "/source")

Add functionality to limit crawling to links that are subdomains of the input URL.

Author - bagarwa2