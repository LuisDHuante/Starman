import time,os
from crawl_osky import crawl_osky
from crawl_solar import crawl_solar

base=os.path.dirname(os.path.realpath(__file__))+"/"

def read_Wait():
	t=.2*60
	
	return int(t)


while(True):
    WaitTime=read_Wait()
    try:
        crawl_osky()
    except:
        pass
    try:
        crawl_solar()
    except:
        pass
    #os.system(f"python3 {base}../01_Database/dbcon.py")
    time.sleep(WaitTime)



