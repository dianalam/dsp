[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> <b>Prompt:</b> Using the variable `totalwgt_lb`, investigate whether first babies are lighter or heavier than others. Compute `Cohen’s d` to quantify the difference between the groups. How does it compare to the difference in pregnancy length?

>> <b>Answer:</b> First babies have a mean weight of `7.20 lbs` and non-first babies have a mean weight of `7.33 lbs`, for a difference in means (Cohen's d) of `0.089 standard deviations`. 

>> Compared to the difference in means of 0.029 standard deviations for difference in height between first/non-first babies, the difference for mean weights is larger, suggesting a more significant difference in weights between first and non-first babies compared to heights. However, a bit of internet research suggests that a Cohen's d of 0.2 is generally regarded as a small effect, 0.5 a moderate effect, and 0.8 a large effect, so a d of 0.089 is still relatively small. 

Code: 

```python
import nsfg
import math

preg = nsfg.ReadFemPreg() 

live = preg[preg.outcome == 1] 
firsts = live[live.birthord == 1] 
others = live[live.birthord > 1]
firstswt = firsts.totalwgt_lb
otherswt = others.totalwgt_lb

def cohensd(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

print 'First babies mean weight (lbs):', firstswt.mean()
print 'Other babies mean weight (lbs):', otherswt.mean()
print 'Difference bw means:', cohensd(firstswt, otherswt), 'std deviations'
```

