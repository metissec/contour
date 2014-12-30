Contour
=======

This contour library uses data given in geographic format, latitude (N°) and longitude (E°). A map is generated from [openstreetmap]([1]) then plotted using matplotlib[2] and geotiler[3] libraries. Then a vector field is generated using gaussian kernel density estimation(KDE) from the scipy library [4] . The input for the KDE are the points provided to the library, which were assigned to a numpy array (np.array()). Then this vector field is applied to the matplotlib.contourf() function. Lastly the points are plotted with simple dots using the matplotlib.scatter() function. This can work on any city in the world, or any location.     

**Algorithm**

Read points into numpy array (np.array()) from a file. 
Find the rough center of points given using the mid point equation. 
Retrieve map from openstreetmap using the center of the points as the center of the map.
Plot the map onto a matplotlib figure.
Using the array of points convert them to cartesian, for use in figure.
Apply this array to a gaussian kernel density estimate (scipy.stats.gaussian_kde()).
Plot the output of the KDE to a contour map (matplotlib.confourf).
Layer the contour map over the map image. With a lower alpha to the contour to make it translucent.
Output figure to PNG file (or any other format supported by matplotlib).  

**Usage**

```python
>>>import contour
>>>contour.Contour(‘File with points’)
```
```
contour.Contour(filename, pix_size=2000, inch_size=10,dpi=200,zoom=14)

	filename: Filename containing points.
	zoom: Zoom of openstreetmap.
	pix_size: Size of image downloaded from open-street map. 
	inch_size: Size of matplotlib figure in inches.
	dpi: Number of pixels per inch of matplotlib figure.
```


**File Format**

The format for the file of points has to be in the format: [latitude,longitude]. Separated by a  comma with no space, and each coordinate has to be be on new line. The file should be plain text ASCII.
	
	Latitude: Has to be in terms of N°. (Incorrect: 1° S  Correct: -1° N )
	
	Longitude: Has to be in terms of E°. (Incorrect: 1° W Correct: -1° E)


**Sample data Random points in London**
					
[Latitude° N, Longitude° E]
```
	51.50308,-0.125999
	51.50308,-0.125999
	51.50308,-0.125999
	51.513123,-0.124626
	51.509704,-0.137501
	51.497523,-0.120678
	51.504041,-0.102825
	51.517609,-0.103168
	51.517823,-0.125484
	51.526261,-0.120506
	51.51793,-0.092354
	51.504148,-0.096989
	51.494317,-0.11364
	51.49111,-0.136642
	51.506926,-0.148487
	51.521028,-0.11879
	51.513657,-0.074158
	51.501904,-0.098362
	51.493568,-0.112438
	51.504575,-0.113983
	51.49763,-0.106602
	51.510345,-0.106602
```
**Reference**
	
[1]: http://openstreetmap.org/ 
[2]: http://matplotlib.org/ 
[3]: http://wrobell.it-zone.org/geotiler/ 
[4]: http://www.scipy.org/
[5]: http://www.numpy.org/
