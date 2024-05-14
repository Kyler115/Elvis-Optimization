import matplotlib.pyplot as plt
from scipy.optimize import minimize
import numpy as np

# Divider line (Intermediate line)
iL = 12
a = [0, 6]  # Line spanning x
b = [iL, iL]  # Line spanning y
plt.plot(a, b)  # Plots line a b
plt.axis([0, 6, 0, 20])  # Shows values for x and y axis

# X points, points to find the optimal path
xX0 = 2  # X value of x0
yX0 = 2  # Y value of x0
xX1 = 5  # X value X1
yX1 = 15  # Y Value of Y1
v0 = 1/2  # Distance / time it takes to get to a point x lambda on the inter from x0 WAS 3/2
v1 = 1/2  # Distance / time it takes to get to a point x lambda on the inter from x1 WAS 1/2
plt.plot(xX0, yX0, 'ro')  # This is x0
plt.plot(xX1, yX1, 'ro')  # This is x1

# Distance to intermediate given a point
def distance_to_inter(x, y):
    return np.abs(iL - y)  # Distance to the intermediate line (y = iL)

# Objective function (total time)
def total_time(points):
    x_lambda = points[0]
    
    d0 = np.sqrt((xX0 - x_lambda)**2 + (yX0 - iL)**2)  # Distance from x0 to x_lambda
    d1 = np.sqrt((x_lambda - xX1)**2 + (yX1 - iL)**2)  # Distance from x_lambda to x1
    
    time_0 = d0 / v0  # Time from x0 to x_lambda
    time_1 = d1 / v1  # Time from x_lambda to x1
    
    return time_0 + time_1  # Total time is the sum of times in 0 and 1

# Optimization
result = minimize(total_time, [xX0], bounds=[(xX0, xX1)])  # Optimization occurs
optimal_x_lambda = result.x[0]  # Finds the optimal x_lambda

# Plot the optimized paths
x_optimized_0_to_lambda = np.linspace(xX0, optimal_x_lambda, 100) # Array of evenly spacced values xX0 and xxlambda
y_optimized_0_to_lambda = np.interp(x_optimized_0_to_lambda, [xX0, optimal_x_lambda], [yX0, iL]) # interpolation between y x based on xlambda
plt.plot(x_optimized_0_to_lambda, y_optimized_0_to_lambda, 'g-', label='Optimized Path (x0 to x_lambda)') # Ploting

#See above, answer in retrospective.
x_optimized_lambda_to_X1 = np.linspace(optimal_x_lambda, xX1, 100)
y_optimized_lambda_to_X1 = np.interp(x_optimized_lambda_to_X1, [optimal_x_lambda, xX1], [iL, yX1])
plt.plot(x_optimized_lambda_to_X1, y_optimized_lambda_to_X1, 'b-', label='Optimized Path (x_lambda to x1)')

plt.plot(optimal_x_lambda, iL, 'ro') # Plots the optimal x lambda on the line iL
plt.legend()
plt.show()
print(optimal_x_lambda, iL)

 