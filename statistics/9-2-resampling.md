[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

>> **Prompt**: In Section 9.3, we simulated the null hypothesis by permutation; that is, we treated the observed values as if they represented the entire population, and randomly assigned the members of the population to the two groups.   
An alternative is to use the sample to estimate the distribution for the population, then draw a random sample from that distribution. This process is called resampling. There are several ways to implement resampling, but one of the simplest is to draw a sample with replacement from the observed values, as in Section 9.10.  
Write a class named `DiffMeansResample` that inherits from `DiffMeansPermute` and overrides `RunModel` to implement resampling, rather than permutation.  
Use this model to test the differences in pregnancy length and birth weight. How much does the model affect the results?

>> **Answer:** 
There is little difference in the permutation and the resampling model; both yield similar p-values and differences in the test statistic. 

Statistic | Results with Permutation | Results with Resampling
---- | ---- | ----
**Birth weight** | 
P-value | 0.0001 | 0.0
Actual diff in wgts | 0.125 | 0.125
Max diff in wgts observed | 0.125| 0.113
**Pregnancy Length** | 
P-value | 0.174 | 0.169 
Actual diff in lengths | 0.078 | 0.078
Max diff in lengths observed | 0.269 | 0.230

Process: 

I modified the `RunModel` method of the `DiffMeansPermute` class and used the provided iPython notebook to run the test stats. 

```python
# create new class and modify runmodel for resampling
class DiffMeansResample(DiffMeansPermute):
    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.n, replace=True)
        return group1, group2

# test preg length
    data = firsts.prglngth.values, others.prglngth.values
    ht = DiffMeansResample(data)
    p_value = ht.PValue(iters=10000)
    print('\nmeans permute preglength')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())

# test birth weight
datawgt = firsts.totalwgt_lb.dropna().values, others.totalwgt_lb.dropna().values
    ht = DiffMeansResample(datawgt)
    p_value = ht.PValue(iters=10000)
    print('\nmeans permute birthweight')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())
```


