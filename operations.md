
## Math Operations:

**addition**
- formula: a + b

**subtraction**
- formula: a – b

**multiplication**
- formula: a x b

**division**
- formula: a÷b

**square root**
- formula: √x = y ⟺ x = y², 
where ⟺ is a mathematical symbol that means if and only if.

**exponentiation** 
- exponential functions are uniquely characterized by the fact that the growth rate of such a function (that is, its derivative) is directly proportional to the value of the function.
- example:  if a stock investment grows every hour. If you start with a stock value of $1 and it doubles every hour, you will have 2x stock price after x hours.
- formula:  f(x) = 2x.

**logarithm** 
- Logarithmic functions are the inverses of exponential functions. 
- The inverse of the exponential function y = ax is x = ay. 
- The logarithmic function y = log(ax) is defined to be equivalent to the exponential equation x = ay.
- 2^3 = 8; therefore, 3 is the logarithm of 8 to base 2, or 3 = log2 8

## Statistical Operations
**mean**
- a type of average
- The "mean" is the "average" you're used to, where you add up all the numbers and then divide by the number of numbers.
- formula: x̄ = ( Σ xi ) / n
x̄ just stands for the “sample mean”
Σ means “add up”
xi “all of the x-values”
n means “the number of items in the sample”
- example: (13 + 18 + 13 + 14 + 13 + 16 + 14 + 21 + 13) ÷ 9 = 15

**medium**
- a type of average
- The "median" is the "middle" value in the list of numbers
-  for list [1,2,3,4,5] the medium = 3

**standard deviation**
- standard deviation is a numerical value used to indicate how widely individuals in a group vary
- σ = sqrt [ Σ ( Xi - X )2 / N ]
- where σ is the population standard deviation, X is the population mean, Xi is the ith element from the population, and N is the number of elements in the population.
- For example, with a sample dataset of 1, 2, 4, 6, the calculation for sample variance would be:
s2 = (( 12 + 22 + 42 + 62) - (1 + 2 + 4 + 6)2/4 ) / (4 - 1) = (57 - (169 / 4)) / 3 = 4.9167
The standard deviation would then be the square root of the variance:
√4.9167 = 2.2

**variance**
- variance is the expectation of the squared deviation of a random variable from its mean.
- formula: pxy = σxy/σx σy
σx and σy are the population standard deviations
σxy is the population covariance.
- example, for the numbers 1, 2, and 3 the mean is 2 and the variance is 0.667. [(1 - 2)2 + (2 - 2)2 + (3 - 2)2] ÷ 3 = 0.667.

**meanDeviation**
- the mean of the absolute values of the numerical differences between the numbers of a set (such as statistical data) and their mean or median
- Mean Deviation =  (Σ|x − μ|)/N
- example:
1. list (2, 5, 7, 10, 12, 14)
1. Find the average: 
8.3 = (2+5+7+10+12+14)/6
1. find the difference between each value and the average. 
2 - 8.3 = 6.3 
5 - 8.3 = 3.3 
7 - 8.3 = 1.3 
10 - 8.3 = 1.7 
12 - 8.3 = 3.7 
14 - 8.3 = 5.7
1. Calculate the average of the differences by adding them and dividing by the number of observations. 
3.66 = (6.3+3.3+1.3+1.7+3.7+5.7) / 6

**quartiles**
- divides the number of data points into four more or less equal parts, or quarters (25%, 50%, 75%)
**example:** 
1.  Put the numbers in order: 1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27.
1. Find the median. 1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27.
1. Place parentheses around the numbers above and below the median. (1, 2, 5, 6, 7), 9, (12, 15, 18, 19, 27).
1. Find Q1 and Q3
Q1  median in the lower half of the data and Q3 is median for the upper half of data.
(1, 2, 5, 6, 7),  9, ( 12, 15, 18, 19, 27). Q1 = 5 and Q3 = 18.
1.  Subtract Q1 from Q3 to find the interquartile range.
18 – 5 = 13.

**convariance**
-  covariance is a measure of the joint variability of two random variables.
- Cov(X,Y) = Σ E((X-μ)E(Y-ν)) / n-1 where: 
X is a random variable. 
E(X) = μ is the expected value (the mean) of the random variable X 
E(Y) = ν is the expected value (the mean) of the random variable Y.
- example: https://corporatefinanceinstitute.com/resources/knowledge/finance/covariance/


**skewness**
-  skewness is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean. 
- Skew = 3 * (Mean – Median) / Standard Deviation.
- for example reference: https://www.spss-tutorials.com/skewness/


##  Population Functions:
**sample correlation**
-  measure how strong a relationship is between two variables. 
- formula: (1/n-1)∑(x-μx) (y-μy)/σxσy
- example showing how it is used: https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/correlation-coefficient-formula/

 **confidence interval sample**
- measures how much uncertainty there is with any particular statistic. Confidence intervals are often used with a margin of error. 
It tells you how confident you can be that the results from a poll or survey reflect what you would expect to find if it were possible to survey the entire population. 
-  formula: X  ±  Zs√n
X is the mean
Z is the chosen Z-value from the table above
s is the standard deviation
n is the number of observations
- example: https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/confidence-interval/

**population proportion**
- A population proportion is a fraction of the population that has a certain characteristic.
- p = x / n
x is the number of items you’re interested in, and
n is the total number of items in the population.
- example: https://www.statisticshowto.datasciencecentral.com/population-proportion/

**conchran**
- The cochran formula allows you to calculate an ideal sample size given a desired level of precision, desired confidence level, and the estimated proportion of the attribute present in the population.
- formula: no = z e ²pq / e ²
e is the desired level of precision (i.e. the margin of error),
p is the (estimated) proportion of the population which has the attribute in question,
q is 1 – p.
z is z-score
- example: https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/find-sample-size/

**confidence interval population**
- confidence interval refers to the percentage of all possible samples that can be expected to include the true population parameter.
- confidence interval = x − 1.645σ/ √ n.
x =  sample mean
n =  sample size
σ =  population standard deviation
- example: https://www.mathsisfun.com/data/confidence-interval.html

**systematic sampling** 
- allows for fair representation of a population
- Systematic Sampling Formula for interval (i) = N/n
N= size of the population
n=size of the sample
- Example:
1.  Assign a number to every element in your population. For this simple example, let’s say you have a population of 100 people, so you’ll assign the numbers 1 to 100 to the group.

1.  Decide how large your sample size should be. See: Sample size (how to find one). For this example, let’s say you need a sample of 10 people.


1.  Divide the population by your sample size.

**sample size unknown**
- used to survey experiments for an unknown population in order to draw inferences for the entire population.
- formula: n= z2
n is the sample size
z is the z-score
 - example: https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/find-sample-size/


**margin of error**
- margin of error tells you how many percentage points your results will differ from the real population value. 
- example: a 95% confidence interval with a 4 percent margin of error means that your statistic will be within 4 percentage points of the real population value 95% of the time.
- formula: MOE =  ((z * σ)/√n)
 σ = sample proportion 
n = sample size,
z = z-score.

**z-score**
- number of standard deviations by which the value of a raw score (i.e., an observed value or data point) is above or below the mean value of what is being observed or measured.
- formula:  z = (x-μ)/σ
x is the raw score
μ is the population mean
σ is the population standard deviation. 
- the z-score is raw score minus the sample mean, divided by the sample standard deviation.
- example of z-score use: https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/z-scores/a/z-scores-review

**population correlation**
-  measure how strong a relationship is between two variables.
- formula and example can be found here: https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/correlation-coefficient-formula/


