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

> Storage Server

In charge of storing up-to-date data with PostgreSQL, to be sorted and retrieved as needed by the Processing Server.

> Processing Server

In charge of generating map images on demand, based on the request by the Web Server API

> Web Server

In charge of displaying map images to the end user through a modern web interface

# General system architecture

# Toolset
The project is to be developed by making use of modern Python 3 libraries, including but not limited to:
* [The OpenSky Network API](https://opensky-network.org/) for data collection of near-real time flight information. 
* [Folium](https://github.com/python-visualization/folium), a wrapper to the [Leaflet.js](https://leafletjs.com/) JavaScript mapping library. | v. 0.12.1
* [NumPy](https://numpy.org/) | v. 1.22.3
* [Pandas](https://pandas.pydata.org/) | v. 1.4.2

Additionally, it plans to make use of the following web technologies, on top of the usual development stack:
* [Apache HTTPD](https://httpd.apache.org/)
* [MariaDB](https://mariadb.org/)
* [PHP](https://www.php.net/)
* [Bootstrap](https://getbootstrap.com/)

# Methodology
...



# Usage Instructions & Requirements
...



# Results
...



# Conclusions
...

# References
Matthias Schäfer, Martin Strohmeier, Vincent Lenders, Ivan Martinovic and Matthias Wilhelm. "Bringing Up OpenSky: A Large-scale ADS-B Sensor Network for Research". In Proceedings of the 13th IEEE/ACM International Symposium on Information Processing in Sensor Networks (IPSN), pages 83-94, April 2014. The [OpenSky Network](https://opensky-network.org)
