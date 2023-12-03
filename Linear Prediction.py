#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Linear Prediction, Acceleration and Gyroscope reading, Graph, Fusion Sensor

import time
import math
import matplotlib.pyplot as plt

initial_latitude = 37.7749
initial_longitude = -122.4194

initial_acceleration = 2.0  # m/s^2
acceleration_change_rate = 0.1  # m/s^2
gyroscope_reading = 0.0  # rad/s
time_step = 1  # seconds

gps_loss_duration = 30  # seconds

# Lists to store coordinates for plotting
latitude_history = [initial_latitude]
longitude_history = [initial_longitude]

def simulate_gps_loss():
    global initial_acceleration

    print("Simulating loss of GPS connection...")

    # Simulate changes in acceleration during GPS loss
    for _ in range(gps_loss_duration):
        initial_acceleration += acceleration_change_rate

    print("GPS connection restored.")

def predict_new_coordinates(direction, imu_fusion=True):
    global initial_latitude, initial_longitude, initial_acceleration, gyroscope_reading
    global latitude_history, longitude_history

    # Simulate prediction based on acceleration and direction
    for _ in range(gps_loss_duration):
        
        if direction == "n":
            initial_latitude += initial_acceleration * time_step
        elif direction == "s":
            initial_latitude -= initial_acceleration * time_step
        elif direction == "e":
            initial_longitude += initial_acceleration * time_step
        elif direction == "w":
            initial_longitude -= initial_acceleration * time_step

        # Fuse sensor measurements using a complementary filter
        if imu_fusion:
            alpha = 0.98
            gyroscope_reading += 0.1
            initial_latitude += alpha * gyroscope_reading * time_step

        # Append coordinates to the history lists
        latitude_history.append(initial_latitude)
        longitude_history.append(initial_longitude)

def plot_coordinates():
    global latitude_history, longitude_history

    plt.plot(longitude_history, latitude_history, marker='o', label='Predicted Path')

    plt.scatter(initial_longitude, initial_latitude, color='red', marker='*', label='Initial Location')

    plt.title('Predicted GPS Coordinates')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.show()



def main():
    global initial_latitude, initial_longitude

    print("Initial GPS Coordinates:")
    print(f"Latitude: {initial_latitude}, Longitude: {initial_longitude}")

    direction = input("Enter the direction (N/S/E/W): ").lower()[0]

    simulate_gps_loss()
    predict_new_coordinates(direction)
    plot_coordinates()

if __name__ == "__main__":
    main()

