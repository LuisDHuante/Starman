import psycopg2,os
import numpy as np
import pandas as pd

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
    
ccsv=f"{base}../current.csv"
cflr=f"{base}../current.flr"
def dump_csv():
    DF=pd.read_csv(ccsv)
    
    FL=read_dict(cflr)
    
    DF.drop(["sensors","geo_altitude","squawk","spi","position_source","vertical_rate","baro_altitude","last_contact"],axis=1,inplace=True)
    DF.dropna()
    DF=DF[DF["on_ground"]!=False].copy()
    
    print(DF.info())
    print(FL)

dconf=read_dict(f"{base}db_logn.conf")

con=psycopg2.connect(host=dconf["host"],port=dconf["port"],database=dconf["database"],user=dconf["user"],password=dconf["password"])
cur=con.cursor()

#try:
dump_csv()
#except:
#	pass

con.commit()
cur.close()
con.close()
