# Reinsurance_Retention

## Project Overview
* Created a tool for insurance companies, which estimates the risk of a change of their reinsurance retention for a specified asset.
* calculates from a claim size distribution in an Excel format a adjusted claim size distribution under a fixed retention and uses the Panjer recursion to calculate the distribution of the sum of claims of a entire asset.
* project of an internship at a major insurance company, which saved reinsurance premium by the calculations.

## Code
**Python Version**: 3.8\
**Packages**: pandas, numpy, matplotlib, seaborn, os

## Results of an example
Shown are the calculated distribution of the sum of claims for various retentions and the change in the expected and probable sum of claims in an realistic (synthetic) example.

<img align="left" width="380" height="400" src="https://raw.githubusercontent.com/Olhaau/Reinsurance_retention/master/SumOfClaims.gif">
<img align="left" width="380" height="385" src="https://raw.githubusercontent.com/Olhaau/Reinsurance_retention/master/EstimatedSafetyCapital.png">
