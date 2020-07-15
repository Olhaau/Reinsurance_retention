<script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
tex2jax: {
inlineMath: [['$','$'], ['\\(','\\)']],
processEscapes: true},
jax: ["input/TeX","input/MathML","input/AsciiMath","output/CommonHTML"],
extensions: ["tex2jax.js","mml2jax.js","asciimath2jax.js","MathMenu.js","MathZoom.js","AssistiveMML.js", "[Contrib]/a11y/accessibility-menu.js"],
TeX: {
extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"],
equationNumbers: {
autoNumber: "AMS"
}
}
});
</script>


# Reinsurance_Retention

## Project Overview
* Created a tool for insurance companies, which makes savings in reinsurance premium possible by controlling the risk of a change of their reinsurance retentions.
* Calculates from a claim size distribution in an Excel format an adjusted claim size distribution under a fixed retention and uses the Panjer recursion to calculate the distribution of the sum of claims of an entire asset.
* Uses the results to estimate the risk of a retention change by calculating the expected sum of claims, the capital for a specified safety, the deviation and more.
* Project of an internship at a major insurance company in 2013, which indeed saved reinsurance premium by the calculations.

## Results of an example
Shown are the calculated distribution of the sum of claims for various retentions and the change in the expected and probable sum of claims in an realistic (synthetic) example.

<img align="left" width="380" height="400" src="https://raw.githubusercontent.com/Olhaau/Reinsurance_retention/master/SumOfClaims.gif">
<img align="left" width="380" height="385" src="https://raw.githubusercontent.com/Olhaau/Reinsurance_retention/master/EstimatedSafetyCapital.png">

## Code
**Python Version**: 3.8\
**Packages**: pandas, numpy, matplotlib, seaborn, os

## Mathematical details
... \\( a^2 = b^2 \\)

### Assumptions
...
