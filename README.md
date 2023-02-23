# Trojan Detection

Names: *Duncan Byrne*, *Jackson Krieger*

Github: *nacnud04*, *jackson-krieger*

## Summary
Use small body orbit information to detect planetary trojans using neural network or other methods.

## Background Information
A trojan is a small celestial body (mostly asteroids) that shares the orbit of a larger body, 
remaining in a stable orbit approximately 60° ahead of or behind the main body near one of its Lagrangian points L4 and L5. 
Trojans can share the orbits of planets or of large moons. 

## Problem Statement
Can we accurately predict if an asteroid is a trojan or not using only orbit information?

## Datasets
NASA small body dataset - https://ssd.jpl.nasa.gov/sb/

## Tools/packages you will use
* Currently not decided/unknown *

## Planned methodology
* Import data
* Remove bad data
* Apply certain filters to the data hopefully crop out the data down to a level where jupiter trojan detection is accurate enough.
* Apply detection method to other planets.

## Expected Outcomes
Hopefully this methodology returns an accuracy of greater than 80%

## Links to references
* https://ssd.jpl.nasa.gov/diagrams/elem_dist.html
* https://ssd.jpl.nasa.gov/tools/sbdb_query.html
* http://www.minorplanetcenter.org/iau/lists/NeptuneTrojans.html
