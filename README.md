# Risk of reinsurance retention changes

## Project Overview
* Created a tool for insurance companies, which makes savings in reinsurance premium possible by controlling the risk of a change of their reinsurance retentions.
* Calculates from a claim size distribution in an Excel format an adjusted claim size distribution under a fixed retention and uses the Panjer recursion to calculate the distribution of the sum of claims of an entire asset.
* Uses the results to estimate the risk of a retention change by calculating the expected sum of claims, the capital for a specified safety, the deviation and more.
* Project of an internship at a major insurance company in 2013, which indeed saved reinsurance premium by the calculations.

## Results of an example
Shown are the calculated distribution of the sum of claims for various retentions and the change in the expected and probable sum of claims in an realistic (synthetic) example.

<img align="left" width="380" height="400" src="https://raw.githubusercontent.com/Olhaau/Reinsurance_retention/master/total_claim.gif">
<img style="float: right;" width="380" height="385" src="https://raw.githubusercontent.com/Olhaau/Reinsurance_retention/master/EstimatedSafetyCapital.png">




## Code
**Python Version**: 3.8\
**Packages**: pandas, numpy, matplotlib, seaborn, os

## Mathematical details
For random variables 
<img src="https://render.githubusercontent.com/render/math?math=X_1, X_2, ...">
(claim sizes) and
<img src="https://render.githubusercontent.com/render/math?math=N">
(number of claims)
with known distributions we want to calculate the distribution of
<img src="https://render.githubusercontent.com/render/math?math=S = \sum_{i = 1}^N X_i">
(total sum of claims). This can be done by Panjer's Algorithm, if we assume the following preconditions.

1. <img src="https://latex.codecogs.com/gif.latex?X_1,&space;X_2,&space;..." title="N, X_1, X_2, ..." /> are independent
2. <img src="https://latex.codecogs.com/gif.latex?X_1,&space;X_2,&space;..." title="X_1, X_2, ..." /> are identically distributed on a lattice <img src="https://latex.codecogs.com/gif.latex?h\mathbb{N}_{0}^{}" title="h\mathbb{N}_{0}^{}" />



## Resources
[Panjer's paper on the algorithm](https://www.casact.org/library/astin/vol12no1/22.pdf)

<!--
TODO:
### -- Under construction --
### Assumptions
...

...
-->

