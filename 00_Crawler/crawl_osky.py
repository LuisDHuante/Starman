from opensky_api import OpenSkyApi
import numpy as np
import pandas as pd
import os

login_u="asphericalcow"
login_p="hktibtl"

api=OpenSkyApi(login_u,login_p)
login_u=None
login_p=None

keys=['icao24', 'callsign', 'origin_country', 'time_position', 'last_contact', 'longitude', 'latitude', 'baro_altitude', 'on_ground', 'velocity', 'true_track', 'vertical_rate', 'sensors', 'geo_altitude', 'squawk', 'spi', 'position_source']

def crawl_osky():
	global api
	data={}
	for k in keys:
		data[k]=[]
	state=api.get_states()
	timestamp=state.time
	filename=f"OS_{timestamp}.csv"
	states=state.states
	for s in states:
		for k in keys:
			data[k].append(s.__dict__[k])
	df=pd.DataFrame()
	for k in keys:
		df[k]=data[k]
	fpath=f"./{int(np.floor(timestamp/(60*60*24))*60*60*24)}/"
	if(not os.path.isdir(fpath)):
		os.mkdir(fpath)
	df.to_csv(fpath+filename)
	df.to_csv("../current.csv")
	return filename
