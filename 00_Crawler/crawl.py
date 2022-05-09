import time
from crawl_osky import crawl_osky
from crawl_solar import crawl_solar

def read_Wait():
	t=.5*60
	
	return int(t)


while(True):
	WaitTime=read_Wait()
	crawl_osky()
	crawl_solar()
	time.sleep(WaitTime)



