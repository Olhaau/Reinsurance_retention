# Reinsurance_Retention

## Project Overview
* Created a tool for insurance companies, which makes savings in reinsurance premium possible by controlling the risk of a change of their reinsurance retentions.
* Calculates from a claim size distribution in an Excel format an adjusted claim size distribution under a fixed retention and uses the Panjer recursion to calculate the distribution of the sum of claims of an entire asset.
* Uses the results to estimate the risk of a retention change by calculating the expected sum of claims, the capital for a specified safety, the deviation and more.
* Project of an internship at a major insurance company, which indeed saved reinsurance premium by the calculations.

## Code
**Python Version**: 3.8\
**Packages**: pandas, numpy, matplotlib, seaborn, os

## Results of an example
Shown are the calculated distribution of the sum of claims for various retentions and the change in the expected and probable sum of claims in an realistic (synthetic) example.

<img align="left" width="380" height="400" src="https://raw.githubusercontent.com/Olhaau/Reinsurance_retention/master/SumOfClaims.gif">
<img align="left" width="380" height="385" src="https://raw.githubusercontent.com/Olhaau/Reinsurance_retention/master/EstimatedSafetyCapital.png">
