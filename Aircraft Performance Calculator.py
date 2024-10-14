# Aircraft Performance Calculator

# Performance calculation code
def calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed):
    range_in_hours = fuel_capacity / fuel_consumption_rate
    range_in_miles = range_in_hours * true_air_speed
    return range_in_miles

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    endurance_in_hours = fuel_capacity / fuel_consumption_rate
    return endurance_in_hours

def calculate_total_weight(payload, fuel_weight):
    return payload + fuel_weight

def calculate_cg_position(moment_list, total_weight):
    total_moment = sum(moment_list)
    cg_position = total_moment / total_weight
    return cg_position

def calculate_moment(weight, arm):
    return weight * arm

def calculate_lift(cl, rho, v, s):
    return 0.5 * cl * rho * v**2 * s

def calculate_drag(cd, rho, v, s):
    return 0.5 * cl * rho * v**2 * s

def calculate_weight(mass, g):
    return mass * g

def calculate_acceleration(thrust, drag, weight, mass):
    return (thrust - drag - weight) / mass

def calculate_velocity(velocity, acceleration, time):
    return velocity + acceleration * time

def calculate_distance(velocity, time):
    return velocity * time

# Values
fuel_capacity = 1000
fuel_consumption_rate = 50
true_air_speed = 150
payload = 5000
fuel_weight = 6000
moment_list = [10000, 2500]
total_weight = 1500
cl = 1.5
rho = 1.225
v = 100
s = 20
cd = 0.02
mass = 5000
g = 9.81
thrust = 6000
drag = 5000
velocity = 50
acceleration = 2
time = 10

range = calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed)
endurance = calculate_endurance(fuel_capacity, fuel_consumption_rate)
total_weight = calculate_total_weight(payload, fuel_weight)
cg_position = calculate_cg_position(moment_list, total_weight)
lift = calculate_lift(cl, rho, v, s)
drag = calculate_drag(cd, rho, v, s)
weight = calculate_weight(mass, g)
acceleration = calculate_acceleration(thrust, drag, weight, mass)
velocity = calculate_velocity(velocity, acceleration, time)
distance = calculate_distance(velocity, time)

def pretty_print(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance):
    pretty_print(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance)

# Save performance values into txt file
def save_info_to_file(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance, file):
    file.write("Performance Calculations:\n")
    file.write("Range: {} miles\n".format(range)) # Can also be coded as file.write("Range: " + str(range) + " miles") but isn't simplified. The .format allows the range to be populated in the curly brackets.
    file.write("Endurance: {} hours\n".format(endurance))
    file.write("Total Weight: {} lbs\n".format(total_weight))
    file.write("Center of Gravity: {} ft\n".format(cg_position))
    file.write("Lift: {} Newtons\n".format(lift))
    file.write("Drag: {} Newtons\n".format(drag))
    file.write("Weight: {} Newtons\n".format(weight))
    file.write("Acceleration: {} m/s^2\n".format(acceleration))
    file.write("Velocity: {} m/s\n".format(velocity))
    file.write("Distance: {} m\n".format(distance))
    file.close()

with open("aircraft_performance_analysis.txt", "w") as f:
    save_info_to_file(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance, file=f) # file=f is another way to introduce a parameter into a function
