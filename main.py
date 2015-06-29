from crawler import *

def main():
	try:
		C = Crawler(str(argv[1]))
		C.Crawl(maxpages = 200, only_sublinks = False)
		#print C.get_links(C.base)

	except (ValueError and IndexError):
		print "No URL specified"

	except:
		print "An unexpected error occured"
	
	print "Crawled a total of " + str(len(C.predecessor)) + " pages"

	# print C.index
	# print C.depth.values()
	# print C.predecessor.values()
	C.save_URLS()
	C.plot()

main()