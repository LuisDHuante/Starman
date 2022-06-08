# STARMAN: Worldwide Flight Visualization & Solar Flare Alert System
## Affiliation

Final Project for the Distributed Computing 2022-2 class, taught by Dr. Victor de la Luz at the _National Autonomous University of Mexico_ (UNAM), in its  National School of Superior-Level Studies, _Morelia_ Campus (ENES Morelia), as part of its _Bs. in Information Technologies applied to Science_ career plan.

> DEVELOPED BY:
>
> Alexis Hassiel Nuviedo Arriaga | alexis.nuviedo@gmail.com | ([@nuviedo](https://github.com/nuviedo))
> 
> Miriam Guadalupe Valdez | mirluvams@gmail.com | ([@mirluvams](https://github.com/mirluvams))
> 
> Luis David Huante García | luisdhuante@gmail.com | ([@LuisDHuante](https://github.com/LuisDHuante))


# Introduction
The following project intends to provide a functional endpoint in which a potential user can visualize a map containing worldwide flight routes in real time. 

The need for such a project stems as a desire to function as a real-time alert system with which to calculate the range in which a solar flare can cause interference with the equipment on board of airships currently flying at high altitudes, given their vulnerability to EMP events.

As a final project, this aims to be a practical demostration of how a series of computers in parallel can be used to obtain an easily scalable product that could potentially be commercialized and expanded upon once completed, without relying on a single, high performance computer to perform the entire process.

# Objectives
The expected output of this project is a set of four servers, each of which provide an essential part of the project. Their denomination is as follows:

> Data Retrieval Server

In charge of obtaining real-time data from the OpenSky Network API, through the use of Python. Will relay said information in a timely manner to the Storage Server, while also keeping copies of recent data points as required for archive purposes.
As measured, the data retrieval process accounts for a 

> Storage Server

In charge of storing up-to-date data with PostgreSQL, to be sorted and retrieved as needed by the Processing Server.

> Processing Server

In charge of generating map images on demand, based on the request by the Web Server API

> Web Server

In charge of displaying map images to the end user through a modern web interface

# General system architecture
![DiagramStarman drawioFinal](https://user-images.githubusercontent.com/69726163/168955379-4be22e91-ad0e-482f-94e3-acfd2e06614d.png)


# Toolset
The project is to be developed by making use of modern Python 3 libraries, including but not limited to:
* [The OpenSky Network API](https://opensky-network.org/) for data collection of near-real time flight information. 
* [Folium](https://github.com/python-visualization/folium), a wrapper to the [Leaflet.js](https://leafletjs.com/) JavaScript mapping library. | v. 0.12.1
* [NumPy](https://numpy.org/) | v. 1.22.3
* [Pandas](https://pandas.pydata.org/) | v. 1.4.2

Additionally, it plans to make use of the following web technologies, on top of the usual development stack:
* [Apache HTTPD](https://httpd.apache.org/)
* [PostgreSQL](https://www.postgresql.org/)

# Methodology

The project was developed in an iterative schedule, adding to critical components on a need-to-use basis, while improving on the previous iterations by replacing outdated code & refactoring necessary details into the implementation.

As such, the project started with the creation of a spider which crawls the required data from the Open Sky API, followed shortly by the creation of a script to insert said data into a PostgreSQL database for further usage.

Following such, the processing script took care of dynamically generating a webpage which contains exclusively the map displaying the final information.

# Usage Instructions & Requirements

The usage of this project requires a very specific folder structure:

* On the data server, Starman/00 should be reachable by crontab and ran as soon as possible with runcol.sh, while the required .cfg files exist in said folder as per the description in its documentation.
* Likewise, Starman/01 should be accessible with the required configuration files as specified in the comments.
* On the processing node, Starman/02 should be available. Starman/03 is implicit as it's stored by default as /data/team1/ for our specific scenario, as defined in 02/getdb.py and 02/processing.py. The configuration files from 01 should be available, so it is recommended to clone the entire project rather than rely on hand updates.


# Results

The result is a real-time updated interactive map that refreshes each minute using the most up to date data, in order to avoid rate limiting. The theoretical time it takes for fresh data to arrive in the database is 10 seconds on average with a standard deviation of 5 seconds, while the time required to generate the map is 7 seconds on average, with standard deviation of 3 seconds mostly tending upwards of 7 than otherwise.




# Conclusions
It is concluded that further work is necessary to provide an usable product to publish to the world, yet the current prototype is functional and can easily be implemented on a distributed system as expected of this project.

The current version of the project, network allowing, should be running in [GICC's Main Page](https://www.gicc.unam.mx/nuviedo/) under a team member's personal redirect.

# References
Matthias Schäfer, Martin Strohmeier, Vincent Lenders, Ivan Martinovic and Matthias Wilhelm. "Bringing Up OpenSky: A Large-scale ADS-B Sensor Network for Research". In Proceedings of the 13th IEEE/ACM International Symposium on Information Processing in Sensor Networks (IPSN), pages 83-94, April 2014. The [OpenSky Network](https://opensky-network.org)
