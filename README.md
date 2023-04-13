# Trojan Detection

Names: *Duncan Byrne*, *Jackson Krieger*

Github: *nacnud04*, *jackson-krieger*

## Summary
Use small body orbit information to detect Jupiter trojans and/or find trends in Jupiter trojan orbit data.

## Background information
A trojan is a small celestial body (mostly asteroids) that shares the orbit of a larger body, 
remaining in a stable orbit approximately 60° ahead of or behind the main body near one of its Lagrangian points L4 and L5. 
Trojans can share the orbits of planets or of large moons. 
Jupiter specifically has over 9800 trojans.

## Problem statement
Can we accurately predict if an asteroid is a trojan and identify orbit data trends by using orbit information?

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
* Remove unnecessary variables from the data to crop it down to a level where Jupiter trojan detection is accurate.
* Develop & train model
* Test model and analyze results.

## Anticipated challenges
* Finding useful parameters and understanding their meaning.
* Predicting if a small body is a trojan via non-distance based parameters.

## Expected outcomes
Hopefully this methodology sorts trojans and non-trojans with an accuracy of greater than 80%

## Summary of results
The filtering methods used resulted in an accuracy of 99.6% which is much higher than originally expected.
We correctly identified 9791 trojans and 3062 non-trojans while incorrectly identifying only 20 trojans and 26 non-trojans.  

## Links to references
* https://ssd.jpl.nasa.gov/diagrams/elem_dist.html
* https://ssd.jpl.nasa.gov/tools/sbdb_query.html
* http://www.minorplanetcenter.org/iau/lists/NeptuneTrojans.html
