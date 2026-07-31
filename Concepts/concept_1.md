# Statistics

Statistics is a branch of mathematics widely used in data-driven fields such as Data Science, Data Analysis, Machine Learning, and Artificial Intelligence.

---

## ✔ Types of Statistics

Statistics is divided into two types:

- **A. Descriptive Statistics**
- **B. Inferential Statistics**

---

## A. Descriptive Statistics

Descriptive statistics is a branch of mathematics that helps summarize, analyze, visualize, and describe the information within a dataset, making it easier to identify hidden patterns in the data.

### Types of Descriptive Statistics

1. **Central Tendency** – Mean (average), Median, Mode
2. **Measure of Dispersion** – Range, Variance, Standard Deviation, IQR
3. **Data Representation** – Charts, Graphs, Tables, Frequency Distributions

---

## 1. Central Tendency

### Mean

- The mean represents the average value of a dataset.
- There are two types of mean:
  1. Population mean
  2. Sample mean

### Median

- When a dataset contains many outliers or is widely scattered, the median is a more reliable measure than the mean.
- The median gives the exact center (middle) value of a dataset.

### Mode

- To know the most occuring value in a dataset, we have to use mode

#### When to use mean and median and mode ??
- When the data is perfect and there is no outliers then we have to use mean
- When the data is not symmetric and contains too much outliers then we have to use median.
- To know the most occuring value.

---
## 2. Measure of Dispersion
<h5>
1. Measure of dispersion helps to measure the spread of each data in a dataset.<br>
2. It helps to identify how much each data is spread from the mean or average.<br>
3. Measure of dispersion helps to identify the distribution of the data.
4. How much the data is scattered from the middle 
</h5>

## ✔ Types

i. **RANGE** - It calculates the difference between maximum and minimum value in a dataset.<br>
ii. **VARIANCE** - It calculates the spread of each data point from the mean / average data point.<br>
iii. **STANDARD DAVIATION** - It measures the actual distance range of each data points from the mean<br>
iv. **IQR** - It identifies where the middle 50% of data is lying.<br>

---

### i. RANGE 
Range is the difference between maximum and minimum value in a given dataset. It helps to measure the spread of each data point from mean or average.

<h4> Formula :<h4>
{R = max - min}

---

### ii. VARIANCE 
Variance helps to measure the spread of each data point from the mean or average. If the variance means the difference of each data point from the mean is low or in close range , then it is highly consistant.If the variance of each data point is too far from the mean or average then it is low consistant or not perfect. We measure the spread of the data points by two types of variance
Such as,

<h5> Types : </h5>
1. Sample variance <br>
2. Population variance

<h3> 1. Sample Variance </h3>
- Measurements are done in a sample dataset.<br>

<h4> Formula :<h4>
s² = Σ(xᵢ − x̄)² / (n − 1)

xi - sample data point <br>
x̄ - sample Mean or average<br>
n - sample size<br>
s² - sample variance

<h3><u> 1. Population Variance </u></h3>
- Measurements are done in whole dataset.<br>

<h4> Formula :<h4>
σ² = Σ(xᵢ − μ)² / N

--- 
### iii. STANDARD DAVIATION
Standard daviation gives the ultimate value after variance which shows a range between lower value to upper value of a data.

<h4> Formula :<h4>
σ = √variance

## Why it is useful ? :
1. By using standard daviation, we can easily measure how much data is close to the average.
2. We usually measure three type of standard daviation. such as,
- **1 SD = 68% of the data**
- **2 SD = 95% of the data**
- **3 SD = 99% of the data**

1 Standard Daviation gives a range where some values falls within that range which is mostly close to the average. We can easily measure how and which data points are mostly close and consistant. which is mostly considered as 68% of the data.

2 Standard Daviation is considered as 95% of the data, by measuring 2 SD, we can easily find out how much data is lying withing the 2nd standard daviation.

3 standard daviation is considered as 99.7% of the data, by measuring 3 SD, we can easily find out how much data is lying below 95% and 68% of the data.

**Note :**
[68% > 95% > 99.7%]
[1SD > 2 SD > 3 SD]