# Trojan Detection

Names: *Duncan Byrne*, *Jackson Krieger*

Github: *nacnud04*, *jackson-krieger*

## Summary
Use small body orbit information to differentiate jupiter trojans, vs non trojan bodies.

## Introduction
A trojan is a small celestial body (mostly asteroids) that shares the orbit of a larger body, 
remaining in a stable orbit approximately 60° ahead of or behind the main body near one of its Lagrangian points L4 and L5. 
This then inherently means that trojan bodies can share the orbits of planets or of large moons. Jupiter specifically
has by far the greatest number of trojans, housing over 9800 bodies.
<br><br>
So, the goal is to see if we can accurately predict if an asteroid is a trojan and identify orbit data trends by using orbit information. This includes more simple parameters such semi-axis distance, as well as some parameters which have less of an obvious correlation. Specifically minimum orbit intersection distance is used.
<br><br>
For parameters with a less obvious correlation such as this a model based on support vector machines is applied.

## Datasets
NASA small body dataset - https://ssd.jpl.nasa.gov/sb/

## Tools/packages you will use

[Pandas](https://pandas.pydata.org/)

[Numpy](https://numpy.org/)

[Matplotlib](https://matplotlib.org/)

[Scikit-learn](https://scikit-learn.org/stable/) 

## Planned methodology
* Import data
* Remove bad data
* Generate plots to visualize trends & better understand relationships between variables
* Remove unnecessary variables from the data to crop it down to a level where Jupiter trojan detection is more efficient and accurate.
* Develop & train model
* Test model and analyze results.

## Summary of results
Applying a simple threshold detection system on the semi-major axis variable, with a cap on eccentricity based on the orbit parameters (perihelion and aphelion of jupiter) resulted in 99.5%
<br><br>
When the model was trained on the following parameters (MOID-earth, MOID-jupiter, eccentricity, perihelion distance) and the other parameters were filtered out, the final model had an accuracy of 99.6% which is much higher than originally expected.
We correctly identified 9791 trojans and 3062 non-trojans while incorrectly identifying only 20 trojans and 26 non-trojans.  

## Links to references
* https://ssd.jpl.nasa.gov/diagrams/elem_dist.html
* https://ssd.jpl.nasa.gov/tools/sbdb_query.html
* http://www.minorplanetcenter.org/iau/lists/NeptuneTrojans.html
