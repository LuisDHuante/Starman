#import psycopg2


dconf={}
with open("db_logn.conf","r") as f:
	L_CONF=[]
	for l in f.read().split("\n"):
		if(len(l)<1):
			continue
		L_CONF.append(l)
	f.close()
	dconf={L.split(":")[0]:L.split(":")[1] for L in L_CONF}
#print(dconf)

con=psycopg2.connect(host=dconf["host"],port=dconf["port"],database=dconf["database"],user=dconf["user"],password=dconf["password"])
