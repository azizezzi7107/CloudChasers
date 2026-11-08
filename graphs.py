import matplotlib.pyplot as plt
import numpy as np

from calculations import calculate_lift, calculate_drag

# Function to plot Lift vs Airspeed

def plot_lift_vs_airspeed(density, wing_area, lift_coefficient):

    # Generate airspeed values
    velocities = np.linspace(10, 300, 100)

    # Calculate lift for each velocity
    lift_values = []

    for velocity in velocities:

        lift = calculate_lift(
            density,
            velocity,
            wing_area,
            lift_coefficient
        )

        lift_values.append(lift)

    # Create the graph
    fig, ax = plt.subplots()

    ax.plot(velocities, lift_values)

    ax.set_title("Lift vs Airspeed")
    ax.set_xlabel("Airspeed (m/s)")
    ax.set_ylabel("Lift Force (N)")

    ax.grid(True)

    return fig

# Function to plot Drag vs Airspeed

def plot_drag_vs_airspeed(density, wing_area, drag_coefficient):

    # Generate airspeed values
    velocities = np.linspace(10, 300, 100)

    # Calculate drag for each velocity
    drag_values = []

    for velocity in velocities:

        drag = calculate_drag(
            density,
            velocity,
            wing_area,
            drag_coefficient
        )

        drag_values.append(drag)

    # Create the graph
    fig, ax = plt.subplots()

    ax.plot(velocities, drag_values)

    ax.set_title("Drag vs Airspeed")
    ax.set_xlabel("Airspeed (m/s)")
    ax.set_ylabel("Drag Force (N)")

    ax.grid(True)

    return fig

# Function to plot Lift-to-Drag Ratio vs Airspeed

def plot_lift_drag_ratio(density, wing_area, lift_coefficient, drag_coefficient):

    velocities = np.linspace(10, 300, 100)

    ratio_values = []

    for velocity in velocities:

        lift = calculate_lift(
            density,
            velocity,
            wing_area,
            lift_coefficient
        )

        drag = calculate_drag(
            density,
            velocity,
            wing_area,
            drag_coefficient
        )

        if drag > 0:
            ratio = lift / drag
        else:
            ratio = 0

        ratio_values.append(ratio)

    # Create the graph
    fig, ax = plt.subplots()

    ax.plot(velocities, ratio_values)

    ax.set_title("Lift-to-Drag Ratio vs Airspeed")
    ax.set_xlabel("Airspeed (m/s)")
    ax.set_ylabel("Lift-to-Drag Ratio")

    ax.grid(True)

    return fig