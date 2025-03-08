# **Report**

## **Part I-A: Network Analysis and Congestion Pricing**

## **Task 1: Network Diagnosis**

### **Problem Statement**

The primary goal of this task is to estimate the user equilibrium flow distribution over the network. Key performance metrics include link volume, travel time, and volume-to-capacity (v/c) ratio. Links with a v/c ratio exceeding 0.90 are classified as bottlenecks.

### **Solution Approach**

1. **Traffic Assignment:** A user equilibrium assignment is performed on the network using the provided link characteristics and the origin-destination trip matrix. The algorithm to calculate the user equilibrium is given in the slides.
2. **Identification of Bottlenecks:** Links with a v/c ratio greater than 0.90 were flagged as bottlenecks.

### **Results and Analysis**

#### **User Equilibrium Flow Distribution**

The equilibrium results provide insight into the network's congestion levels. The table below highlights links where congestion is critical (v/c ≥ 0.90):

| Link | Volume (veh/hr) | Travel Time (min) | v/c  |
|------|-----------------|-------------------|------|
| 1    | 4193.2          | 4.0               | 0.93 |
| 2    | 10546.8         | 3.3               | 1.24 |
| 3    | 4700.0          | 3.2               | 0.41 |
| 4    | 11203.2         | 3.1               | 0.73 |
| 5    | 11940.0         | 2.4               | 0.26 |
| 6    | 8852.2          | 2.4               | 0.26 |
| 7    | 10334.8         | 2.4               | 0.26 |
| 8    | 9195.5          | 2.4               | 0.36 |
| 9    | 13403.5         | 1.2               | 0.48 |
| 10   | 7608.3          | 3.6               | 0.90 |
| 11   | 15538.3         | 1.2               | 0.33 |
| 12   | 8569.9          | 2.5               | 0.64 |
| 13   | 6113.4          | 3.1               | 0.61 |
| 14   | 11290.0         | 3.9               | 1.20 |
| 15   | 8449.7          | 2.6               | 0.90 |
| 16   | 10253.5         | 1.0               | 0.49 |
| 17   | 4890.0          | 1.8               | 0.32 |
| 18   | 4380.0          | 1.2               | 0.09 |
| 19   | 10220.1         | 1.5               | 1.10 |
| 20   | 4380.0          | 1.8               | 0.29 |
| 21   | 1713.5          | 1.8               | 0.18 |
| 22   | 4160.0          | 3.0               | 0.43 |
| 23   | 7578.4          | 3.0               | 0.39 |
| 24   | 1720.1          | 2.0               | 0.18 |
| 25   | 7826.9          | 1.8               | 0.29 |
| 26   | 9298.5          | 1.8               | 0.34 |
| 27   | 6127.6          | 3.0               | 0.31 |
| 28   | 8410.6          | 3.6               | 0.32 |
| 29   | 1829.8          | 3.0               | 0.19 |
| 30   | 1975.0          | 4.2               | 0.21 |
| 31   | 5886.7          | 3.7               | 0.63 |
| 32   | 5884.7          | 3.0               | 0.30 |
| 33   | 5704.8          | 3.7               | 0.61 |
| 34   | 10734.4         | 3.0               | 1.15 |
| 35   | 11384.8         | 2.4               | 0.25 |
| 36   | 3364.6          | 3.6               | 0.36 |
| 37   | 12360.3         | 1.8               | 0.24 |
| 38   | 11070.0         | 1.8               | 0.22 |
| 39   | 10300.3         | 2.9               | 1.06 |
| 40   | 10310.1         | 2.9               | 1.11 |
| 41   | 4968.4          | 3.0               | 0.51 |
| 42   | 7396.6          | 2.5               | 0.79 |
| 43   | 8869.2          | 3.2               | 0.33 |
| 44   | 3930.2          | 3.0               | 0.40 |
| 45   | 5642.7          | 2.5               | 0.62 |
| 46   | 9931.9          | 2.4               | 0.49 |
| 47   | 3610.0          | 3.0               | 0.38 |
| 48   | 1739.8          | 3.0               | 0.18 |
| 49   | 4160.0          | 1.2               | 0.42 |
| 50   | 1829.8          | 1.8               | 0.05 |
| 51   | 1940.9          | 4.2               | 0.20 |
| 52   | 3610.0          | 1.2               | 0.36 |
| 53   | 6135.0          | 1.2               | 0.67 |
| 54   | 4890.0          | 1.2               | 0.11 |
| 55   | 1739.8          | 1.8               | 0.04 |
| 56   | 6209.8          | 2.6               | 0.82 |
| 57   | 4107.6          | 2.8               | 1.05 |
| 58   | 5550.9          | 1.2               | 0.60 |
| 59   | 5141.4          | 2.4               | 0.54 |
| 60   | 6629.8          | 2.8               | 0.87 |
| 61   | 4732.1          | 2.6               | 0.85 |
| 62   | 5525.1          | 3.7               | 0.58 |
| 63   | 3186.7          | 3.0               | 0.33 |
| 64   | 5512.1          | 3.7               | 0.57 |
| 65   | 7291.8          | 1.5               | 0.73 |
| 66   | 11026.6         | 2.4               | 1.19 |
| 67   | 10257.5         | 2.4               | 0.51 |
| 68   | 2430.5          | 2.8               | 0.25 |
| 69   | 7925.3          | 1.3               | 0.79 |
| 70   | 4267.5          | 2.4               | 0.45 |
| 71   | 7200.6          | 2.5               | 0.77 |
| 72   | 5160.4          | 2.4               | 0.54 |
| 73   | 5399.3          | 1.2               | 0.56 |
| 74   | 10720.0         | 2.7               | 0.98 |
| 75   | 10280.0         | 2.2               | 1.11 |
| 76   | 6096.2          | 1.2               | 0.63 |

**Bottleneck Links:**

| Link | v/c Ratio |
|------|-----------|
| 1    | 0.93      |
| 2    | 1.24      |
| 10   | 0.90      |
| 14   | 1.20      |
| 15   | 0.90      |
| 19   | 1.10      |
| 34   | 1.15      |
| 39   | 1.06      |
| 40   | 1.11      |
| 57   | 1.05      |
| 66   | 1.19      |
| 74   | 0.98      |
| 75   | 1.11      |

**Total System Travel Time:** **1,262,792.44 minutes**

### **Discussion**

The analysis reveals severe congestion on multiple links, particularly **Links 1, 2, 10, 14, etc(shown in the table Bottleneck Links)**, where demand significantly exceeds capacity. This underscores the necessity of traffic management strategies such as congestion pricing to enhance network performance.

---

## **Task 2: Marginal-Cost Pricing**

### **Problem Statement**

The objective of this task is to determine the system optimum flow distribution and compute marginal-cost tolls that, when implemented, replicate the system optimum under user equilibrium conditions.

### **Solution Approach**

1. **System Optimum Assignment:** Compute link flows that minimize total system travel time. Compared with UE solver, when doing all-or-nothing assignment, the travel time needs to be replaced with the marginal cost of travel time.
2. **Marginal-Cost Toll Calculation:** Derive tolls based on the additional system delay caused by an extra vehicle. This can be done by calculating the derivative of the total travel time with respect to the flow on each link.

### **Results and Analysis**

#### **Comparison of System Optimum and User Equilibrium with Tolls**

| Link | SO Flow (veh/hr) | Toll (min) | UE Flow (veh/hr) |
|------|------------------|------------|------------------|
| 1    | 4600.1           | 2.36       | 4495.3           |
| 2    | 10032.1          | 2.79       | 10144.0          |
| 3    | 3267.6           | 0.01       | 3255.1           |
| 4    | 11717.9          | 0.60       | 11606.0          |
| 5    | 13264.6          | 0.01       | 13284.2          |
| 6    | 8467.2           | 0.01       | 8644.4           |
| 7    | 10107.8          | 0.01       | 10115.8          |
| 8    | 10455.6          | 0.04       | 10336.3          |
| 9    | 14120.7          | 0.05       | 14367.4          |
| 10   | 5196.3           | 0.28       | 5113.4           |
| 11   | 15933.5          | 0.01       | 16023.9          |
| 12   | 8562.7           | 0.24       | 8563.7           |
| 13   | 6842.1           | 0.39       | 7079.3           |
| 14   | 9965.4           | 2.27       | 9945.8           |
| 15   | 7004.6           | 0.44       | 7427.5           |
| 16   | 12163.9          | 0.07       | 12001.6          |
| 17   | 4715.4           | 0.01       | 4771.0           |
| 18   | 4515.0           | 0.00       | 4480.8           |
| 19   | 8853.3           | 0.59       | 9205.1           |
| 20   | 4515.0           | 0.01       | 4480.8           |
| 21   | 4010.7           | 0.03       | 3637.5           |
| 22   | 4160.0           | 0.06       | 4160.0           |
| 23   | 9422.9           | 0.10       | 9082.0           |
| 24   | 1728.0           | 0.00       | 1726.3           |
| 25   | 10331.0          | 0.02       | 10440.1          |
| 26   | 10629.1          | 0.02       | 10531.6          |
| 27   | 8310.3           | 0.06       | 8619.0           |
| 28   | 10735.1          | 0.06       | 10717.1          |
| 29   | 1823.0           | 0.00       | 1825.9           |
| 30   | 2020.8           | 0.01       | 2020.5           |
| 31   | 5441.9           | 0.25       | 5218.9           |
| 32   | 6145.6           | 0.02       | 6203.4           |
| 33   | 5558.8           | 0.26       | 5787.2           |
| 34   | 8422.7           | 0.97       | 8394.6           |
| 35   | 11351.9          | 0.01       | 11564.0          |
| 36   | 3330.2           | 0.04       | 3254.6           |
| 37   | 12184.7          | 0.00       | 12257.7          |
| 38   | 11200.1          | 0.00       | 11173.3          |
| 39   | 10113.5          | 1.70       | 10191.1          |
| 40   | 7932.3           | 0.76       | 7817.0           |
| 41   | 4511.2           | 0.08       | 4156.7           |
| 42   | 6534.8           | 0.34       | 6609.8           |
| 43   | 11287.0          | 0.06       | 11363.2          |
| 44   | 3209.2           | 0.02       | 2782.6           |
| 45   | 5776.7           | 0.23       | 5778.7           |
| 46   | 10561.2          | 0.11       | 10495.6          |
| 47   | 2931.7           | 0.02       | 2984.5           |
| 48   | 2049.1           | 0.00       | 1792.1           |
| 49   | 4160.0           | 0.02       | 4160.0           |
| 50   | 1823.0           | 0.00       | 1825.9           |
| 51   | 2325.6           | 0.01       | 2535.5           |
| 52   | 3360.8           | 0.01       | 3040.6           |
| 53   | 6180.8           | 0.15       | 6180.5           |
| 54   | 4715.4           | 0.00       | 4771.0           |
| 55   | 1620.0           | 0.00       | 1736.0           |
| 56   | 6338.0           | 0.70       | 6306.7           |
| 57   | 3086.3           | 0.56       | 3205.9           |
| 58   | 5686.4           | 0.11       | 5576.1           |
| 59   | 5440.0           | 0.15       | 5370.2           |
| 60   | 6335.3           | 0.75       | 6507.0           |
| 61   | 3965.4           | 0.36       | 3903.1           |
| 62   | 5868.5           | 0.30       | 5744.1           |
| 63   | 4154.5           | 0.06       | 4067.7           |
| 64   | 5345.8           | 0.21       | 5507.1           |
| 65   | 6560.8           | 0.16       | 5924.1           |
| 66   | 8776.7           | 0.86       | 8369.4           |
| 67   | 11871.5          | 0.18       | 11710.3          |
| 68   | 2419.9           | 0.01       | 2257.8           |
| 69   | 6507.5           | 0.13       | 5579.5           |
| 70   | 6114.7           | 0.25       | 6544.4           |
| 71   | 6536.4           | 0.34       | 6596.3           |
| 72   | 6326.9           | 0.28       | 6294.6           |
| 73   | 6840.0           | 0.18       | 7747.8           |
| 74   | 10839.0          | 1.41       | 10816.8          |
| 75   | 8207.3           | 0.66       | 8377.1           |
| 76   | 7053.9           | 0.20       | 7484.5           |
**Performance Metrics:**
- **Total System Travel Time:** **1,249,222.53 minutes**
- **Total Toll Revenue (converted to time equivalent):** **187,672.19 minutes**

### **Discussion**

The system optimum flow distribution closely aligns with the user equilibrium when tolls are applied. Implementing marginal-cost pricing leads to significant improvements in total travel time, reducing overall congestion.

---

## **Task 3: Pricing with Constraints**

### **Problem Statement**

This task aims to develop a congestion pricing scheme under real-world constraints:
- Only five links can be tolled.
- Maximum toll per link is limited to 3 minutes.
- The goal is to achieve the greatest reduction in total system travel time.

### **Solution Approach**

1. **Identify Key Links:** Select the most congested links where limited tolling can yield maximum system-wide benefits. Here we decided to use the bottleneck links with **the top 5 highest v/c ratios**.
2. **Toll Optimization:** Determine the optimal tolls under the imposed constraints. Since the tolls are within 3 minutes, **I discretized the tolls to 0.5, 1.0, 1.5, 2.0, 2.5, and 3.0 minutes, and for each of five links, I tried all combinations of tolls, and select the combination that gives the lowest total system travel time.**

### **Results and Analysis**

#### **Optimal Tolling Scheme**

| Link | Toll (min) |
|------|------------|
| 2    | 0.5        |
| 14   | 1.5        |
| 66   | 0.5        |
| 34   | 1.0        |
| 40   | 1.0        |

**Performance Metrics:**
- **Total System Travel Time with Optimal Tolls:** **1,253,993.79 minutes**
- **Total System Travel Time without Tolls:** **1,262,792.44 minutes**
- **Reduction in Total Travel Time:** **8,798.65 minutes**

### **Discussion**

Although constrained tolling does not achieve the full efficiency of marginal-cost pricing, it still provides a **measurable reduction in congestion**. By targeting the most critical links, this approach demonstrates that **even a limited tolling strategy can significantly improve network performance.**

---

## Part I-B: Network Design


### Problem Statement

Design an optimal improvement plan that selects among the candidate projects to minimize the total system travel time under the following constraints:

- Candidate new road segments and capacity expansions have specified construction costs.
- The total budget is limited to $60 million.

### Solution Procedure

1. Since there are 6 new road segments and 2 capacity expansions, and for each of them, there are 3 options, so 
   there are 3^8 = 6561 possible combinations.

2. Traverse all combinations and calculate the total system travel time for each combination.

3. Select the combination that minimizes the total system travel time while staying within the budget.

### Analysis Results

**Optimal Improvement Plan:**

| Improvement Option           | Cost  |
|------------------------------|-------|
| Build A#1_1                  | $12M  |
| Build B#2_2                  | $16M  |
| Build C#1_1                  | $15M  |
| Build C#2_1                  | $12M  |
| Expand Link 2 (Option 1)     | $3M   |
| Expand Link 57 (Option 1)    | $2M   |
| **Total Cost**               | **$60M** |

**Performance Metrics:**

| Metric                                             | Value (vehicle-minutes) |
|----------------------------------------------------|-------------------------|
| Total System Travel Time with Improvements (UE)   | 1,210,819.21            |
| Total System Travel Time without Improvements (UE)| 1,262,448.08            |
| Reduction in UE Travel Time                        | 51,628.87               |
| System Optimum Travel Time (SO)                    | 1,249,544.86            |
| Difference from SO                                 | 38,725.65               |

### Discussion

From the chart we can see that the optimal improvement plan reduces the total system travel time by 38,725.65  minutes compared to the original system optimum. This is a significant improvement, demonstrating the effectiveness of targeted infrastructure investments.

---