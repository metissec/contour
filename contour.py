#!/usr/bin/python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import geotiler
from scipy.stats import gaussian_kde


class Contour():

    def __init__(self, in_f,pix_size=2000,inch_size=10,dpi=200,zoom=14):

        #init varibles
        self.in_f = in_f
        self.np = np
        self.plt = plt
        self.zoom = zoom
self.pix_size = pix_size
        self.inch_size = inch_size
        self.dpi = dpi

        #start fig
        self.fig = self.plt.figure(figsize=(self.inch_size, self.inch_size), dpi=self.dpi)
        self.ax = self.plt.subplot(111)

        #init func.
        self.cor_array()

    def bounds(self):

        #min/max
        xmin = self.a[:,0].min()
        xmax = self.a[:,0].max()
        ymin = self.a[:,1].min()
        ymax = self.a[:,1].max()

        #center
        midx = (xmax + xmin)/2
        midy = (ymax + ymin)/2
        self.center = (float(midx), float(midy))

        self.map_l()

    def map_l(self):

        #download map and plot map
        self.mm = geotiler.Map(center=self.center, zoom=self.zoom, size =(self.pix_size,self.pix_size))
        self.img = geotiler.render_map(self.mm)
        self.ax.imshow(self.img)
        self.contour_l()

    def cor_array(self):

        #open file
        f = open(self.in_f,"r")
        #init array
        initline = f.readline()
        initline = initline.rstrip('\n')
        initline = tuple(float(x) for x in initline.split(","))
        self.a = np.array((initline[1],initline[0]))
        #put rest of data into array
        for line in f:
            if line == '\n':
                break
            line = line.rstrip('\n')
            line = tuple(float(x) for x in line.split(","))
            b = np.array((line[1],line[0]))
            self.a = np.vstack((self.a,b))

        self.bounds()

    def contour_l(self):

        #lat,long to x,y
        x, y = zip(*(self.mm.rev_geocode(p) for p in self.a))
        self.a = np.array([x,y])

        #data shaping
        X, Y = np.mgrid[0:self.pix_size:100j, 0:self.pix_size:100j]
        positions = np.vstack([X.ravel(),Y.ravel()])
        kernel = gaussian_kde(self.a)
        Z = np.reshape(kernel(positions).T, X.shape)

        #plot
        self.ax.contourf(X,Y,Z,cmap='rainbow',alpha=.5,linewidth=.4)
        self.ax.scatter(x, y, c='black', edgecolor='white', s=10, alpha=0.9)

        self.layer_out()

   
 def layer_out(self):

        #remove tics
        self.plt.gca().xaxis.set_major_locator(plt.NullLocator())
        self.plt.gca().yaxis.set_major_locator(plt.NullLocator())

        #output png
        self.plt.savefig('test.png', bbox_inches='tight')
        self.plt.close()

Contour('pnts_ny.txt')
