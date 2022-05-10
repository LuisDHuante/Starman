import psycopg2,os

base=os.path.dirname(os.path.realpath(__file__))+"/"

def read_dict(path):
    with open(path,"r") as f:
        L_CONF=[]
        for l in f.read().split("\n"):
            if(len(l)<1):
                continue
            L_CONF.append(l)
        f.close()
        dconf={L.split(":")[0]:L.split(":")[1] for L in L_CONF}

ccsv=f"{base}../current.csv"
cflr=f"{base}../current.flr"
def dump_csv():
    DF=pd.read_csvA(ccsv)
    FL=read_dict(cflr)
    print(DF.info())
    print(FL)

dconf=read_dict(f"{base}db_logn.conf")

con=psycopg2.connect(host=dconf["host"],port=dconf["port"],database=dconf["database"],user=dconf["user"],password=dconf["password"])
cur=con.cursor()

try:
	dump_csv()
except:
	pass

con.commit()
cur.close()
con.close()
