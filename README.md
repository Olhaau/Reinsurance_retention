# Reinsurance_Retention

## Project Overview
* Created a tool for insurance companies, which estimates the risk of a change of their reinsurance retention for a specified asset. 
* calculates from a claim size distribution in Excel a adjusted claim size distribution under a fixed retention and uses the Panjer recursion to calculate the distribution of the sum of claims of a entire asset.

## Code
**Python Version**: 3.8

**Packages**: pandas, numpy, matplotlib, seaborn, os

## Results of an example
Shown are the calculated distribution of the sum of claims dependent of the retention and the change in the expected and probable sum of claims in an realistic example.

<img align="left" width="450" height="420" src="https://raw.githubusercontent.com/Olhaau/Reinsurance_retention/master/SumOfClaims.gif">
<img align="right" width="450" height="405" src="https://raw.githubusercontent.com/Olhaau/Reinsurance_retention/master/EstimatedSafetyCapital.png">
