#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#PID CONTROLLER

import numpy as np
import matplotlib.pyplot as plt

#Quadcopter parameters
mass = 5
g = 9.81

# PID controller parameters
kp = 100.0
ki = 55.0
kd = 8.0

# Simulation parameters
dt = 0.01
total_time = 20.0
num_steps = int(total_time / dt)

""""# Sensor noise parameters
gyro_noise_stddev = 0.1
accel_noise_stddev = 0.1"""

# Target angle in degrees
target_angle_degrees = 22.5
initial_angle_from_imu_degrees = 45

# Convert degrees to radians
target_angle = np.radians(target_angle_degrees)
initial_angle_from_imu = np.radians(initial_angle_from_imu_degrees)

# Initialize state variables
theta = initial_angle_from_imu
theta_dot = 0.0  # Angular velocity
integral = 0.0  # Integral of error for the integral term

time = np.linspace(0, total_time, num_steps)
theta_data = np.zeros(num_steps)

for i in range(num_steps):
    
    """gyro_measurement = theta_dot + np.random.normal(0, gyro_noise_stddev)
    accel_measurement = -g * np.sin(theta) + np.random.normal(0, accel_noise_stddev)"""

    # PID controller
    error = target_angle - theta
    integral += error * dt
    derivative = (error - theta_dot) / dt

    # Control input
    u = kp * error + ki * integral + kd * derivative

    # Update state variables using dynamics
    theta_dot += (u - mass * g * np.sin(theta)) / mass * dt
    theta += theta_dot * dt

    theta_data[i] = theta

theta_data_degrees = np.degrees(theta_data)
target_angle_degrees = np.degrees(target_angle)

plt.plot(time, theta_data_degrees, label='Quadcopter Angle')
plt.axhline(y=target_angle_degrees, color='r', linestyle='--', label='Target Angle')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.legend()
plt.title('Quadcopter PID Control to Reach Target Angle')
plt.show()

