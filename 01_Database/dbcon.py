import psycopg2,psycopg2.extras,os
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
cols=["icao24", "callsign", "origin_country", "time_position", "longitude", "latitude", "velocity", "true_track"]
def dump_csv(con,cur):
    DF=pd.read_csv(ccsv)
    
    FL=read_dict(cflr)
    
    DF.drop(["Unnamed: 0","sensors","geo_altitude","squawk","spi","position_source","vertical_rate","baro_altitude","last_contact"],axis=1,inplace=True)
    DF.dropna(inplace=True)
    DF=DF[DF["on_ground"]==False].copy()
    DF.drop(["on_ground"],axis=1,inplace=True)
    
    print(DF.info())
    print(FL)
    
    cur.execute("DELETE FROM Flights;")
    T=[]
    for t in DF.iterrows():
        S=t[1]
        L=[]
        for c in cols:
            L.append(S[c])
        T.append(tuple(L))
    psycopg2.extras.execute_values(cur,f"INSERT INTO Flights VALUES %s;",T)
dconf=read_dict(f"{base}db_logn.conf")

con=psycopg2.connect(host=dconf["host"],port=dconf["port"],database=dconf["database"],user=dconf["user"],password=dconf["password"])
cur=con.cursor()

#try:
dump_csv(con,cur)
#except:
#	pass

con.commit()
cur.close()
con.close()
