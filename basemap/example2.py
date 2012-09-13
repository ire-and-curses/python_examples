#!/usr/bin/env python

'''
example3.py - Blue marble example from
http://matplotlib.sourceforge.net/basemap/doc/html/users/geography.html

Author: Eric Saunders
March 2011
'''

from __future__ import division
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

sites = { 
          'OGG' : {'lat':20.7069444444, 'long':-156.258055556},
          #'SQA' : {'lat':34.6914533333, 'long':-120.042221667},
          'SBA' : {'lat':34.43276111, 'long':-119.8629306},
          'COJ' : {'lat':-31.273, 'long':149.070593},
          'LSC' : {'lat':-30.1673666667, 'long':-70.8049}
         }



centre_lat = 38
centre_lon = -118
width = 7.5
height = 7.5
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
m = Basemap(
            #width=1200000,height=900000,
            projection='lcc',
            resolution='c',
            lat_0 = centre_lat,
            lon_0 = centre_lon,
 #           lat_1 = 20,
 #           lon_1 = -105,
 #           lat_2 = 50,
 #           lon_2 = -135,
            llcrnrlat = centre_lat - height,
            llcrnrlon = centre_lon - width,
            urcrnrlat = centre_lat + height,
            urcrnrlon = centre_lon + width,
            )
m.bluemarble()
#m.drawcoastlines()
#m.drawrivers()
m.drawstates()
m.drawcountries()

#site_lon = sites['SQA']['long']
#site_lat = sites['SQA']['lat']
scaling = 1
#x,y = m([site_lon-width/scaling, site_lon+width/scaling, ],
#        [site_lat, site_lat,])

#m.plot(x, y, '-', color='red')
#m.drawgreatcircle(site_lon-width/scaling, site_lat,
#                  site_lon+width/scaling, site_lat,
#                  del_s=100.0, color='red')


#x,y = m([site_lon, site_lon], [site_lat-height/scaling, site_lat+height/scaling])
#m.plot(x, y, '-', color='red')
#m.drawgreatcircle(x, y, '-', color='red')


for site in sites:
    print site, sites[site]['lat'], sites[site]['long']
    xpt, ypt = m(sites[site]['long'], sites[site]['lat'])
    m.plot([xpt],[ypt], color='#ee7766', marker='o')

plt.savefig('background3.png')

