import numpy as np

# Define the original series of numbers, prescaled sample
x = [53,70,64,74,54,71,54,65,60,62,69,58,63,62,52,43,51,46,69,66,59,50,62,62,62,74,71,60,60,68,62,55,63,66,81,68,64,73,70,71]

# Calculate the mean, median, and variance of the original series
mean = np.mean(x)
median = np.median(x)
variance = np.var(x)

# Standardize the original series using z-score normalization
z = (x - mean) / np.sqrt(variance)

# Define the desired mean, median, and variance for the scaled series
Emam_and_modaress=[74,78,75,71,80,70,68,75,80,79,74,80,85,87,86,89,81,86,86,85,88,89,89,80,76,89,81,65,83,70,81,83,66,65,80,78,83,89,90,75,87,90,89,90,87,91,82,65,90,76,92,93,93,92,92,92,76
]
#mean of emam_and_modaress
desired_mean = 81
#median of emam_and_modaress
desired_median = 83
#variance of emam and modaress
desired_variance = 63

# Scale the standardized scores to the desired mean, median, and variance
y = (z * np.sqrt(desired_variance)) + desired_mean
y=np.round(y,0)
# Print the scaled series
for i in range(0,len(x)):
    x[i]=(x[i],y[i])
print(x)
