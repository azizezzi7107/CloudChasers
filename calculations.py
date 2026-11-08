# Aircraft Flight Calculations

def calculate_speed(distance, time):
    if time <= 0:
        raise ValueError("Time must be greater than zero.")

    speed = distance / time
    return speed


def calculate_distance(speed, time):
    if speed < 0 or time < 0:
        raise ValueError("Speed and time cannot be negative.")

    distance = speed * time
    return distance


def calculate_time(distance, speed):
    if speed <= 0:
        raise ValueError("Speed must be greater than zero.")

    if distance < 0:
        raise ValueError("Distance cannot be negative.")

    time = distance / speed
    return time

# Aerodynamics Calculations

# Function to calculate lift
def calculate_lift(density, velocity, wing_area, lift_coefficient):

    lift = 0.5 * density * (velocity ** 2) * wing_area * lift_coefficient

    return lift


# Function to calculate drag
def calculate_drag(density, velocity, wing_area, drag_coefficient):

    drag = 0.5 * density * (velocity ** 2) * wing_area * drag_coefficient

    return drag

# Aircraft Performance Calculations

# Calculate Wing Loading
def calculate_wing_loading(weight, wing_area):

    if wing_area <= 0:
        raise ValueError("Wing area must be greater than zero.")

    wing_loading = weight / wing_area

    return wing_loading


# Calculate Thrust-to-Weight Ratio
def calculate_thrust_weight_ratio(thrust, weight):

    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")

    ratio = thrust / weight

    return ratio


# Calculate Power-to-Weight Ratio
def calculate_power_weight_ratio(power, mass):

    if mass <= 0:
        raise ValueError("Mass must be greater than zero.")

    ratio = power / mass

    return ratio


# Calculate Aspect Ratio
def calculate_aspect_ratio(wingspan, wing_area):

    if wing_area <= 0:
        raise ValueError("Wing area must be greater than zero.")

    ratio = (wingspan ** 2) / wing_area

    return ratio