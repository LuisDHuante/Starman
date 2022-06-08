import psycopg2,psycopg2.extras,os
import numpy as np
import pandas as pd
from process import make_image

base=os.path.dirname(os.path.realpath(__file__))+"/"

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


dconf=read_dict(f"{base}../01_Database/db_logn.conf")

con=psycopg2.connect(host=dconf["host"],port=dconf["port"],database=dconf["database"],user=dconf["user"],password=dconf["password"])
#conf=psycopg2.connect(host=dconf["host"],port=dconf["port"],database="testing",user=dconf["user"],password=dconf["password"])
cur=con.cursor()
#curf=conf.cursor()

#try:
cur.execute("SELECT * FROM flights;")
flights=cur.fetchall()
#curf.execute("SELECT * FROM flares;")
#flares=curf.fetchall()

#conf.commit()
con.commit()
cur.close()
#curf.close()
con.close()
#conf.close()

make_image(flights,[])

#except:
#	pass
