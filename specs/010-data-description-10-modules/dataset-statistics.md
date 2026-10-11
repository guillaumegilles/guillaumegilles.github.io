# Dataset Statistics for Module Authoring

*Generated on 2026-10-11 from `wandering-fork.csv`*

## Harbour -- 120d

### Daily Revenue (EUR)
- **n**: 120
- **mean**: 413.4872
- **median**: 391.4650
- **mode**: No unique mode
- **min**: 51.2100
- **max**: 1050.0000
- **range**: 998.7900
- **var_s**: 46661.1039
- **std_s**: 216.0118
- **cv**: 0.5224
- **q1**: 267.8900
- **q3**: 567.3150
- **iqr**: 299.4250
- **lower_fence**: -181.2475
- **upper_fence**: 1016.4525
- **skew_scipy**: 0.4696
- **skew_excel**: 0.4696
- **pearson_skew**: 0.3058

### Customer Count
- **n**: 120
- **mean**: 30.4333
- **median**: 27.0000
- **mode**: 25
- **min**: 5
- **max**: 78
- **range**: 73
- **var_s**: 244.6846
- **std_s**: 15.6424
- **cv**: 0.5140
- **q1**: 21.0000
- **q3**: 39.7500
- **iqr**: 18.7500
- **lower_fence**: -7.1250
- **upper_fence**: 67.8750
- **skew_scipy**: 0.5868
- **skew_excel**: 0.5868
- **pearson_skew**: 0.6585

### Temperature (degC)
- **n**: 120
- **mean**: 23.9300
- **median**: 23.8500
- **mode**: 21.9000
- **min**: 13.7000
- **max**: 32.0000
- **range**: 18.3000
- **var_s**: 11.4285
- **std_s**: 3.3806
- **cv**: 0.1413
- **q1**: 21.9000
- **q3**: 26.3500
- **iqr**: 4.4500
- **lower_fence**: 15.2250
- **upper_fence**: 33.0250
- **skew_scipy**: -0.0811
- **skew_excel**: -0.0811
- **pearson_skew**: 0.0710

### Foot Traffic
- **n**: 120
- **mean**: 49.0583
- **median**: 43.0000
- **mode**: 41
- **min**: 10
- **max**: 133
- **range**: 123
- **var_s**: 549.0806
- **std_s**: 23.4325
- **cv**: 0.4776
- **q1**: 35.0000
- **q3**: 59.0000
- **iqr**: 24.0000
- **lower_fence**: -1.0000
- **upper_fence**: 95.0000
- **skew_scipy**: 1.1896
- **skew_excel**: 1.1896
- **pearson_skew**: 0.7756

### Weather Frequency
| weather   |   count |   rel_% |   cum_% |
|:----------|--------:|--------:|--------:|
| Cloudy    |      42 |   35    |   35    |
| Rainy     |      25 |   20.83 |   55.83 |
| Sunny     |      53 |   44.17 |  100    |

### Satisfaction Rating Frequency
|   satisfaction_rating |   count |   rel_% |   cum_% |
|----------------------:|--------:|--------:|--------:|
|                     1 |       4 |    3.33 |    3.33 |
|                     2 |      21 |   17.5  |   20.83 |
|                     3 |      40 |   33.33 |   54.16 |
|                     4 |      45 |   37.5  |   91.66 |
|                     5 |      10 |    8.33 |   99.99 |

### Weather x Promo Contingency (row %)
| weather   |    No |   Yes |
|:----------|------:|------:|
| Cloudy    | 88.1  | 11.9  |
| Rainy     | 92    |  8    |
| Sunny     | 84.91 | 15.09 |
| All       | 87.5  | 12.5  |

### Regression: Customers -> Revenue
- **n**: 120
- **slope**: 12.3971
- **intercept**: 36.2012
- **r**: 0.8977
- **r2**: 0.8059
- **covariance**: 3033.3864

### Regression: Temperature -> Revenue
- **n**: 120
- **slope**: 4.1541
- **intercept**: 314.0799
- **r**: 0.0650
- **r2**: 0.0042
- **covariance**: 47.4750

## Harbour -- 30d

### Daily Revenue (EUR)
- **n**: 30
- **mean**: 628.3417
- **median**: 643.6300
- **mode**: No unique mode
- **min**: 407.5900
- **max**: 886.5600
- **range**: 478.9700
- **var_s**: 18793.3268
- **std_s**: 137.0888
- **cv**: 0.2182
- **q1**: 506.6050
- **q3**: 729.9925
- **iqr**: 223.3875
- **lower_fence**: 171.5237
- **upper_fence**: 1065.0738
- **skew_scipy**: 0.0337
- **skew_excel**: 0.0337
- **pearson_skew**: -0.3346

### Customer Count
- **n**: 30
- **mean**: 48.0333
- **median**: 44.0000
- **mode**: 38
- **min**: 31
- **max**: 78
- **range**: 47
- **var_s**: 157.8264
- **std_s**: 12.5629
- **cv**: 0.2615
- **q1**: 38.0000
- **q3**: 56.0000
- **iqr**: 18.0000
- **lower_fence**: 11.0000
- **upper_fence**: 83.0000
- **skew_scipy**: 0.8082
- **skew_excel**: 0.8082
- **pearson_skew**: 0.9632

### Temperature (degC)
- **n**: 30
- **mean**: 22.6500
- **median**: 22.6000
- **mode**: 21.9000
- **min**: 16.4000
- **max**: 27.1000
- **range**: 10.7000
- **var_s**: 8.8047
- **std_s**: 2.9673
- **cv**: 0.1310
- **q1**: 20.3750
- **q3**: 24.9750
- **iqr**: 4.6000
- **lower_fence**: 13.4750
- **upper_fence**: 31.8750
- **skew_scipy**: -0.1915
- **skew_excel**: -0.1915
- **pearson_skew**: 0.0506

### Foot Traffic
- **n**: 30
- **mean**: 79.0667
- **median**: 72.0000
- **mode**: 56
- **min**: 47
- **max**: 133
- **range**: 86
- **var_s**: 499.2368
- **std_s**: 22.3436
- **cv**: 0.2826
- **q1**: 61.5000
- **q3**: 92.2500
- **iqr**: 30.7500
- **lower_fence**: 15.3750
- **upper_fence**: 138.3750
- **skew_scipy**: 0.7438
- **skew_excel**: 0.7438
- **pearson_skew**: 0.9488

### Weather Frequency
| weather   |   count |   rel_% |   cum_% |
|:----------|--------:|--------:|--------:|
| Cloudy    |      12 |   40    |   40    |
| Rainy     |       5 |   16.67 |   56.67 |
| Sunny     |      13 |   43.33 |  100    |

### Satisfaction Rating Frequency
|   satisfaction_rating |   count |   rel_% |   cum_% |
|----------------------:|--------:|--------:|--------:|
|                     2 |       6 |   20    |   20    |
|                     3 |       6 |   20    |   40    |
|                     4 |      16 |   53.33 |   93.33 |
|                     5 |       2 |    6.67 |  100    |

### Weather x Promo Contingency (row %)
| weather   |    No |   Yes |
|:----------|------:|------:|
| Cloudy    | 88.1  | 11.9  |
| Rainy     | 92    |  8    |
| Sunny     | 84.91 | 15.09 |
| All       | 87.5  | 12.5  |

### Regression: Customers -> Revenue
- **n**: 30
- **slope**: 9.6797
- **intercept**: 163.3949
- **r**: 0.8871
- **r2**: 0.7869
- **covariance**: 1527.7075

### Regression: Temperature -> Revenue
- **n**: 30
- **slope**: 28.7130
- **intercept**: -22.0086
- **r**: 0.6215
- **r2**: 0.3862
- **covariance**: 252.8084

## Campus -- 120d

### Daily Revenue (EUR)
- **n**: 120
- **mean**: 455.0281
- **median**: 390.3900
- **mode**: No unique mode
- **min**: 23.8500
- **max**: 1407.5900
- **range**: 1383.7400
- **var_s**: 94511.7974
- **std_s**: 307.4277
- **cv**: 0.6756
- **q1**: 236.0650
- **q3**: 598.6000
- **iqr**: 362.5350
- **lower_fence**: -307.7375
- **upper_fence**: 1142.4025
- **skew_scipy**: 0.9999
- **skew_excel**: 0.9999
- **pearson_skew**: 0.6308

### Customer Count
- **n**: 120
- **mean**: 38.8417
- **median**: 34.0000
- **mode**: 42
- **min**: 3
- **max**: 106
- **range**: 103
- **var_s**: 587.2436
- **std_s**: 24.2331
- **cv**: 0.6239
- **q1**: 21.2500
- **q3**: 49.0000
- **iqr**: 27.7500
- **lower_fence**: -20.3750
- **upper_fence**: 90.6250
- **skew_scipy**: 0.7886
- **skew_excel**: 0.7886
- **pearson_skew**: 0.5994

### Temperature (degC)
- **n**: 120
- **mean**: 22.9117
- **median**: 23.4000
- **mode**: 23.5000
- **min**: 13.5000
- **max**: 30.7000
- **range**: 17.2000
- **var_s**: 15.6948
- **std_s**: 3.9617
- **cv**: 0.1729
- **q1**: 20.2250
- **q3**: 26.2000
- **iqr**: 5.9750
- **lower_fence**: 11.2625
- **upper_fence**: 35.1625
- **skew_scipy**: -0.1801
- **skew_excel**: -0.1801
- **pearson_skew**: -0.3698

### Foot Traffic
- **n**: 120
- **mean**: 70.2333
- **median**: 62.0000
- **mode**: 85
- **min**: 5
- **max**: 166
- **range**: 161
- **var_s**: 1807.6930
- **std_s**: 42.5170
- **cv**: 0.6054
- **q1**: 43.2500
- **q3**: 84.7500
- **iqr**: 41.5000
- **lower_fence**: -19.0000
- **upper_fence**: 147.0000
- **skew_scipy**: 0.7524
- **skew_excel**: 0.7524
- **pearson_skew**: 0.5809

### Weather Frequency
| weather   |   count |   rel_% |   cum_% |
|:----------|--------:|--------:|--------:|
| Cloudy    |      48 |   40    |   40    |
| Rainy     |      22 |   18.33 |   58.33 |
| Sunny     |      50 |   41.67 |  100    |

### Satisfaction Rating Frequency
|   satisfaction_rating |   count |   rel_% |   cum_% |
|----------------------:|--------:|--------:|--------:|
|                     1 |       4 |    3.33 |    3.33 |
|                     2 |      39 |   32.5  |   35.83 |
|                     3 |      46 |   38.33 |   74.16 |
|                     4 |      29 |   24.17 |   98.33 |
|                     5 |       2 |    1.67 |  100    |

### Weather x Promo Contingency (row %)
| weather   |     No |   Yes |
|:----------|-------:|------:|
| Cloudy    |  87.5  | 12.5  |
| Rainy     | 100    |  0    |
| Sunny     |  90    | 10    |
| All       |  90.83 |  9.17 |

### Regression: Customers -> Revenue
- **n**: 120
- **slope**: 12.3007
- **intercept**: -22.7506
- **r**: 0.9696
- **r2**: 0.9401
- **covariance**: 7223.4930

### Regression: Temperature -> Revenue
- **n**: 120
- **slope**: -9.4731
- **intercept**: 672.0733
- **r**: -0.1221
- **r2**: 0.0149
- **covariance**: -148.6791

## Campus -- 30d

### Daily Revenue (EUR)
- **n**: 30
- **mean**: 514.6073
- **median**: 440.5200
- **mode**: No unique mode
- **min**: 23.8500
- **max**: 1407.5900
- **range**: 1383.7400
- **var_s**: 108756.3811
- **std_s**: 329.7823
- **cv**: 0.6408
- **q1**: 293.7225
- **q3**: 668.5150
- **iqr**: 374.7925
- **lower_fence**: -268.4663
- **upper_fence**: 1230.7038
- **skew_scipy**: 1.2060
- **skew_excel**: 1.2060
- **pearson_skew**: 0.6740

### Customer Count
- **n**: 30
- **mean**: 43.6000
- **median**: 38.0000
- **mode**: 20
- **min**: 3
- **max**: 106
- **range**: 103
- **var_s**: 665.8345
- **std_s**: 25.8038
- **cv**: 0.5918
- **q1**: 26.5000
- **q3**: 56.7500
- **iqr**: 30.2500
- **lower_fence**: -18.8750
- **upper_fence**: 102.1250
- **skew_scipy**: 0.7910
- **skew_excel**: 0.7910
- **pearson_skew**: 0.6511

### Temperature (degC)
- **n**: 30
- **mean**: 19.6000
- **median**: 19.7000
- **mode**: 16.3000
- **min**: 13.5000
- **max**: 26.6000
- **range**: 13.1000
- **var_s**: 11.1572
- **std_s**: 3.3402
- **cv**: 0.1704
- **q1**: 16.4750
- **q3**: 22.0250
- **iqr**: 5.5500
- **lower_fence**: 8.1500
- **upper_fence**: 30.3500
- **skew_scipy**: 0.1961
- **skew_excel**: 0.1961
- **pearson_skew**: -0.0898

### Foot Traffic
- **n**: 30
- **mean**: 78.2667
- **median**: 70.0000
- **mode**: 85
- **min**: 12
- **max**: 166
- **range**: 154
- **var_s**: 2028.8230
- **std_s**: 45.0425
- **cv**: 0.5755
- **q1**: 44.0000
- **q3**: 121.0000
- **iqr**: 77.0000
- **lower_fence**: -71.5000
- **upper_fence**: 236.5000
- **skew_scipy**: 0.5242
- **skew_excel**: 0.5242
- **pearson_skew**: 0.5506

### Weather Frequency
| weather   |   count |   rel_% |   cum_% |
|:----------|--------:|--------:|--------:|
| Cloudy    |      10 |   33.33 |   33.33 |
| Rainy     |       3 |   10    |   43.33 |
| Sunny     |      17 |   56.67 |  100    |

### Satisfaction Rating Frequency
|   satisfaction_rating |   count |   rel_% |   cum_% |
|----------------------:|--------:|--------:|--------:|
|                     1 |       1 |    3.33 |    3.33 |
|                     2 |       7 |   23.33 |   26.66 |
|                     3 |      14 |   46.67 |   73.33 |
|                     4 |       8 |   26.67 |  100    |

### Weather x Promo Contingency (row %)
| weather   |     No |   Yes |
|:----------|-------:|------:|
| Cloudy    |  87.5  | 12.5  |
| Rainy     | 100    |  0    |
| Sunny     |  90    | 10    |
| All       |  90.83 |  9.17 |

### Regression: Customers -> Revenue
- **n**: 30
- **slope**: 12.2768
- **intercept**: -20.6632
- **r**: 0.9606
- **r2**: 0.9228
- **covariance**: 8174.3486

### Regression: Temperature -> Revenue
- **n**: 30
- **slope**: -24.3429
- **intercept**: 991.7276
- **r**: -0.2466
- **r2**: 0.0608
- **covariance**: -271.5993
