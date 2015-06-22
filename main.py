from crawler import *

def main():
	try:
		C = Crawler(str(argv[1]))
		#print C.open()
		#print "Opened the Base page"
		C.Crawl(maxpages = 100)
		#print C.get_links(C.base)
		print C.index
		print C.depth.values()
		print C.predecessor.values()
		C.save_URLS()

	except (ValueError and IndexError):	
		print "No URL specified"

	except:
		print "An unexpected error occured"


main()