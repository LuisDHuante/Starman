import time,os
from crawl_osky import crawl_osky

def read_dict(path):
	ret=None
	with open(path,"r") as f:
		L_CONF=[]
		for l in f.read().split("\n"):
			if(len(l)<1):
				continue
			L_CONF.append(l)
		f.close()
		ret={L.split(":")[0]:L.split(":")[1] for L in L_CONF}
	return ret

base=os.path.dirname(os.path.realpath(__file__))+"/"

def read_Wait():
	d=read_dict(f"{base}time.cfg")
	t=d["delay"]
	
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
	os.system(f"python3 {base}../01_Database/dbcon.py")
	time.sleep(WaitTime)



