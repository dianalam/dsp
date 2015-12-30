[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> <b>Prompt:</b> In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters `μ = 178 cm` and `σ = 7.7 cm` for men, and `μ = 163 cm` and `σ = 7.3 cm` for women.

>> In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range?  

>> As a bonus (optional) step, write out the null hypothesis, alternative hypothesis, critical value for testing, and the associated p-value.  You will see p-values in virtually every algorithm output during the bootcamp.  And from this exercise, you will know how the p-value has been computed and its relationship to a distribution.

>> <b>Answer:</b> Approximately 34.27% of of the male population is in the Blue Man Group range of 5'10" to 6'1". 

>> <b>Null hypothesis:</b> 
<br><b>Alternative hypothesis:</b>
<br><b>Critical value for testing:</b>
<br><b>P-value:</b> 

I used `scipy.stats.norm` to create a normal distribution using the given mean of 178 cm and standard deviation of 7.7. 

```python
import thinkstats2
import thinkplot
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
```

Then I wrote a short function to convert the Blue Man Group heights from the English measurement system over to metric units. 

```python
# define function to convert from ft/in to cm
def eng2met(ft, inch):
    inches = (ft * 12) + inch
    cm = 2.54 * inches
    return cm

low = eng2met(5, 10) # set low end of height range
high = eng2met(6, 1) # set high end of height range 
```

To determine the percentage of the male population from the normal distribution in the Blue Man Group height range, I subtracted the CDF of the 5'10" height from the CDF of 6'1" height. 

```python
pctInRange = dist.cdf(high) - dist.cdf(low)
print('Pct of male pop in BMG range:', pctInRange * 100)
```

