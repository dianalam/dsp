[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Actual mean of number of children in hh: 1.024
>> Observed mean of number of children in hh: 2.40

<img src="img/ch3ex.jpg">

Code Using Thinkstats Modules: 
```python
import seaborn as sns
import numpy as np
import thinkstats2
import thinkplot
import matplotlib.pyplot as plt 
import chap01soln

def BiasPmf(pmf, label=''): # from chap03ex.ipynb
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

resp = chap01soln.ReadFemResp()

actual_pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
biased_pmf = BiasPmf(actual_pmf, label='observed')

thinkplot.Pmfs([actual_pmf, biased_pmf]) # plotting
plt.xlabel('Number of Children')
plt.ylabel('PMF')
plt.legend()
plt.title('Actual vs. Observed Number of Children in HH')
plt.savefig('../../dsp/img/ch3ex.jpg')
plt.show()

actualMean = tsPmf.Mean() # calculate and print means
observedMean = biased_pmf.Mean()
print 'Actual mean:', actualMean
print 'Observed/biased mean:', observedMean
```

Alternate Code without Thinkstats:
```python
plthist = plt.hist(resp.numkdhh, bins=np.arange(0,7,1), align='left', normed = True) # plot pmf using matplotlib
plt.legend(('num children in hh',))
plt.show()

#calculate pmf mean 
hist = {}
for x in resp.numkdhh:
    hist[x] = hist.get(x, 0) + 1

n = float(sum(hist.values()))
manual_pmf = {}
for x, freq in hist.items():
    manual_pmf[x] = freq / n 

def pmfmean(dict):
    mean = 0.0
    for x, p in dict.items():
        mean += p * x
    return mean

print pmfmean(manual_pmf)
```