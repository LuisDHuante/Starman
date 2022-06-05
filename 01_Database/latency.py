import numpy as np
import pandas as pd

D=[]
with open("timestamps.idata","r") as f:
    D=f.read().split("\n")
    D.pop()
    D=[float(x) for x in D]
    D=pd.Series(D)
    f.close()
print(D.describe())
