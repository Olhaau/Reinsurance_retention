# Risk of reinsurance retention changes

## Project Overview
* Created a tool for insurance companies, which makes savings in reinsurance premium possible by controlling the risk of a change in their reinsurance retentions.
* Calculates from a claim size distribution in an Excel format an adjusted claim size distribution under a fixed retention and uses the Panjer recursion to calculate the distribution of the sum of claims of an entire asset.
* Uses the results to estimate the risk of a retention change by calculating the expected sum of claims, the capital for a specified safety, the deviation and more.
* Project of an internship at a major insurance company in 2013 that indeed made savings in reinsurance premium possible


## Results of an example
Shown are the calculated distribution of the sum of claims for various retentions and the change in the expected and probable sum of claims in an realistic (synthetic) example.

<img align="left" width="380" height="400" src="https://raw.githubusercontent.com/Olhaau/Reinsurance_retention/master/total_claim.gif">
<img style="float: right;" width="380" height="385" src="https://raw.githubusercontent.com/Olhaau/Reinsurance_retention/master/EstimatedSafetyCapital.png">


## Code
**Python Version**: 3.8\
**Packages**: pandas, numpy, matplotlib, seaborn, os

## Mathematical details
For random variables 
<img src="https://latex.codecogs.com/gif.latex?X_1,&space;X_2,&space;..." title="X_1, X_2, ..." />
(claim sizes) and a 
<img src="https://latex.codecogs.com/gif.latex?\mathbb{N}_0" title="\mathbb{N}_0" />-valued random variable
<img src="https://latex.codecogs.com/gif.latex?N" title="N" />
(number of claims)
with known distributions we want to calculate the distribution of
<img src="https://latex.codecogs.com/gif.latex?S&space;=&space;\sum_{i&space;=&space;1}^{N}&space;X_i" title="S = \sum_{i = 1}^{N} X_i" />
(total sum of claims). We assume the following preconditions.

1. <img src="https://latex.codecogs.com/gif.latex?N,&space;X_1,&space;X_2,&space;..." title="N, X_1, X_2, ..." /> are independent
2. <img src="https://latex.codecogs.com/gif.latex?X_1,&space;X_2,&space;..." title="X_1, X_2, ..." /> are identically distributed on a lattice <img src="https://latex.codecogs.com/gif.latex?h\mathbb{N}_{0}^{}" title="h\mathbb{N}_{0}^{}" /> with latticewidth <img src="https://latex.codecogs.com/gif.latex?h>0" title="h>0" /> 
and <img src="https://latex.codecogs.com/gif.latex?f_k&space;=&space;P(X_i&space;=&space;hk)" title="f_k = P(X_i = hk))" /> for each <img src="https://latex.codecogs.com/gif.latex?i,&space;k&space;\in&space;\mathbb{N}_0" title="k \in \mathbb{N}_0" />. In actuarial practice <img src="https://latex.codecogs.com/gif.latex?X_i" title="X_i" /> is obtained by discretisation of the claim density function.
3. <img src="https://latex.codecogs.com/gif.latex?N" title="N" /> is Poisson, binomial or negativ binomial distributed

Then the distribution of <img src="https://latex.codecogs.com/gif.latex?S" title="N" /> can be calculated by Panjer's algorithm. Setting <img src="https://latex.codecogs.com/gif.latex?p_k&space;=&space;P(N&space;=&space;k)" title="P(N = k) = p_k" />  and <img src="https://latex.codecogs.com/gif.latex?g_k&space;=&space;P(S=hk)" title="g_k = P(S=hk)" /> we have  
  
   
<p align=center><img src="https://latex.codecogs.com/gif.latex?g_0&space;=&space;p_0\cdot&space;\exp(f_0&space;b)" title="g_0 = p_0\cdot \exp(f_0 b)" /></p> 
   if <img src="https://latex.codecogs.com/gif.latex?N" title="g_k = P(S=hk)" /> is Poisson distributed and else 
  <p align=center><img src="https://latex.codecogs.com/gif.latex?g_0&space;=&space;\tfrac{p_0}{(1-f_0a)^{1+b/a}}" title="g_0 = p_0\cdot \exp(f_0 b)" />  </p>
   and proceed with  
<p align=center><img src="https://latex.codecogs.com/gif.latex?g_k&space;=&space;\tfrac{1}{1-f_0a}\sum_{j=1}^k(a&plus;\tfrac{b\cdot&space;j}{k})\cdot&space;f_j&space;\cdot&space;g_{k-j}" title="g_k = \tfrac{1}{1-f_0a}\sum_{j=1}^k(a+\tfrac{b\cdot j}{k})\cdot f_j \cdot g_{k-j}" />  </p>

where ![im](https://latex.codecogs.com/gif.latex?a) and ![im](https://latex.codecogs.com/gif.latex?b) can be calculated by

| Distribution of ![im](https://latex.codecogs.com/gif.latex?N) | Parameters  | ![im](https://latex.codecogs.com/gif.latex?a) | ![im](https://latex.codecogs.com/gif.latex?b) 
| :------------------ | :-----------------: | :-----------------: | :-----------------: |
| Binomial            |  ![im](https://latex.codecogs.com/gif.latex?n\in\mathbb{N}), ![im](https://latex.codecogs.com/gif.latex?p\in(0,1))                   |                      ![im](https://latex.codecogs.com/gif.latex?-p/(1-p))      |  ![im](https://latex.codecogs.com/gif.latex?(n+1)p/(1-p))            |
| Negative binomial   | ![im](https://latex.codecogs.com/gif.latex?r\in(0,\infty)), ![im](https://latex.codecogs.com/gif.latex?p\in(0,1))                    |                      ![im](https://latex.codecogs.com/gif.latex?1-p)  |  ![im](https://latex.codecogs.com/gif.latex?(r-1)(1-p))                |
| Poisson             | ![im](https://latex.codecogs.com/gif.latex?\lambda\in(0,\infty))                    | ![im](https://latex.codecogs.com/gif.latex?0)                     | ![im](https://latex.codecogs.com/gif.latex?\lambda)                    |





## Resources
[Panjer's paper on the algorithm](https://www.casact.org/library/astin/vol12no1/22.pdf), see also
[wiki](https://en.wikipedia.org/wiki/Panjer_recursion)

<!--
TODO:
### -- Under construction --
### Assumptions
...
h<sub>&theta;</sub>(x) = &theta;<sub>o</sub> x + &theta;<sub>1</sub>x

, it follows that <img src="https://latex.codecogs.com/gif.latex?a,&space;b" title="a, b" /> exists with <img src="https://latex.codecogs.com/gif.latex?a+b\geq&space;0" title="a, b" /> and <img src="https://latex.codecogs.com/gif.latex?p_k&space;=&space;(a&space;&plus;\tfrac{b}{k})\cdot&space;p_{k-1}" title="p_k = (a +\tfrac{b}{k})\cdot p_{k-1}" /> for <img src="https://latex.codecogs.com/gif.latex?k\geq&space;1" title="g_0 = p_0\cdot \exp(f_0 b)" />.  


| Distribution of ![im](https://latex.codecogs.com/gif.latex?N)   | Binomial         | Negativ binomial  | Poisson           |   
| :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| Parameters        | ![im](https://latex.codecogs.com/gif.latex?n\in\mathbb{N}), ![im](https://latex.codecogs.com/gif.latex?p\in(0,1))   | ![im](https://latex.codecogs.com/gif.latex?r\in(0,\infty)), ![im](https://latex.codecogs.com/gif.latex?p\in(0,1))            | ![im](https://latex.codecogs.com/gif.latex?\lambda\in(0,\infty))              |
| ![im](https://latex.codecogs.com/gif.latex?a)      | ![im](https://latex.codecogs.com/gif.latex?-p/(1-p))  | ![im](https://latex.codecogs.com/gif.latex?1-p)            | ![im](https://latex.codecogs.com/gif.latex?0)               |
| ![im](https://latex.codecogs.com/gif.latex?b)      | ![im](https://latex.codecogs.com/gif.latex?(n+1)p/(1-p))  | ![im](https://latex.codecogs.com/gif.latex?(r-1)(1-p))            | ![im](https://latex.codecogs.com/gif.latex?\lambda)              |

...
-->

