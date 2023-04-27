# Trojan Detection

Names: *Duncan Byrne*, *Jackson Krieger*

Github: *nacnud04*, *jackson-krieger*

## Summary
Use small body orbit information to differentiate jupiter trojans, vs non trojan bodies.

## Introduction
A trojan is a small celestial body (mostly asteroids) that shares the orbit of a larger body, 
remaining in a stable orbit approximately 60° ahead of or behind the main body near one of its Lagrangian points L4 and L5. 
This then inherently means that trojan bodies can share the orbits of planets or of large moons. Jupiter specifically
has by far the greatest number of trojans, housing over 9800 bodies. Hence it was used for this study.
<br><br>
So, the goal is to see if we can accurately predict if an asteroid is a trojan and identify orbit data trends by using orbital information. This includes more simple parameters such semi-axis distance, as well as some parameters which have less of an obvious correlation. Such as minimum orbit intersection distance, eccentricity, or luminosity
<br><br>
Two different methods of trojan detection are applied. The first is a simple hand measured threshold applied to the data. The second method is based on a support vector machines model. This model will be used to see if detection can be better performed by training a model on parameters where correlation is less obvious.
<br><br>
References for all of this information are listed below.

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
Applying a simple threshold detection system on the semi-major axis variable based on the orbit parameters (perihelion and aphelion of jupiter), and capping eccentricity at 0.3 resulted in 99.5% accuracy.
<br><br>
When the model was trained on the following parameters (MOID-earth, MOID-jupiter, eccentricity, perihelion distance) and the other parameters were filtered out, the final model had an accuracy of 99.6% which is much higher than originally expected.
We correctly identified 9791 trojans and 3062 non-trojans while incorrectly identifying only 20 trojans and 26 non-trojans.  
<br><br>
This shows that jupiter trojan/non-trojans can be differentiated by other orbital parameters relating to distance. However most all other parameters are absolutely useless for this classification. For example, when variables such as luminosity or time based parameters were plotted, there was absolutely no correlation so a model was not even trained.
<br><br>
From the difference in the accuracy of the threshold model, versus the trained model it is clear that while there was a small improvement, the benefits of training a model vs doing a simple threshold are essentially 0. Therefore, due to efforts of making and training a model, in most all applications this would not be worth the effort.

## Contribution statement
**Duncan** - *Did most of the theory work and programming* 
<br><br>
**Jackson** - *Worked on analysing input variables and figuring out which parameters should be omitted from testing*

## Links to references
* https://ssd.jpl.nasa.gov/diagrams/elem_dist.html
* https://ssd.jpl.nasa.gov/tools/sbdb_query.html
* http://www.minorplanetcenter.org/iau/lists/NeptuneTrojans.html

## Reference notebook
* https://github.com/GPGN-268/FP-02-Trojans/blob/main/notebooks/final.ipynb
