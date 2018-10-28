## Newsvendor Models: How Many NFL Replica Jerseys to Order so that Profits Are Maximized?

This notebook shows how to solve the NFL Replica Jerseys / Newsvendor problem in Python from the lectures in MITx's CTL.SC1x: Supply Chain Fundamentals. To take the course, please visit https://www.edx.org/micromasters/mitx-supply-chain-management.

1. The Problem
2. The Dataset
3. The Models
4. Conclusion

**1. Motivation**

The problem is as follows: In 2002, Reebok had the sole rights to sell NFL football jerseys. Peak sales for the jerseys last about 8 weeks, while the lead time for manufacturing is 12-16 weeks. That means if sales take off in Week 1, it is already too late to order more jerseys. In short, Reebok had to commit to one order in advance, without knowing actual demand and without any ability to course correct after the order was placed.

**2. The Dataset**

Demand for the jerseys was normally distributed with a mean of 32,000 and a standard deviation of 11,000.

**3. The Model**
This is a classic case of the newsvendor problem. Newsvendor models are characterized by probabilistic demand and single period planning horizons.

**4. Conclusion**

By using a risk-sharing buyback contract, the ideal order was increased from 40,149 to 43,122 resulting in a profit increase of $75,541 for the retailer and $23,784 for the manufacturer.
