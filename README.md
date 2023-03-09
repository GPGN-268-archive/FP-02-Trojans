# Trojan Detection

Names: *Duncan Byrne*, *Jackson Krieger*

Github: *nacnud04*, *jackson-krieger*

## Summary
Use small body orbit information to detect jupiter trojans and/or find trends in jupiter trojan orbit data.

## Background Information
A trojan is a small celestial body (mostly asteroids) that shares the orbit of a larger body, 
remaining in a stable orbit approximately 60° ahead of or behind the main body near one of its Lagrangian points L4 and L5. 
Trojans can share the orbits of planets or of large moons. 
Jupiter specifically has over 9800 trojans.

## Problem Statement
Can we accurately predict if an asteroid is a trojan and identify orbit data trends by mainly using orbit information?

## Datasets
NASA small body dataset - https://ssd.jpl.nasa.gov/sb/

## Tools/packages you will use
[Pandas](https://pandas.pydata.org/)
[Numpy](https://numpy.org/)

## Planned methodology
* Import data
* Remove bad data
* Generate plots to visualize trends & better understand relationships between variables
* Apply certain filters to the data hopefully crop out the data down to a level where jupiter trojan detection is accurate enough.
* Check filter accuracy

## Anticipated challenges
* Predicting if a small body is a trojan based on time based parameters.

## Expected Outcomes
Hopefully this methodology returns an accuracy of greater than 80%

## Links to references
* https://ssd.jpl.nasa.gov/diagrams/elem_dist.html
* https://ssd.jpl.nasa.gov/tools/sbdb_query.html
* http://www.minorplanetcenter.org/iau/lists/NeptuneTrojans.html
