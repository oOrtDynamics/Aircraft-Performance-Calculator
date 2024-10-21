from pyscript import document

def calculate_range(fuel_capacity, fuel_consumption_rate, true_airspeed):
    range_in_hours = float(fuel_capacity) / float(fuel_consumption_rate)
    range_in_miles = range_in_hours * float(true_airspeed)
    return range_in_miles

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    endurance_in_hours = float(fuel_capacity) / float(fuel_consumption_rate)
    return endurance_in_hours

def calculate_total_weight(payload, fuel_weight, weight):
    return payload + fuel_weight + weight

def calculate_cg_position(moment_index, total_weight):
    cg_position =  float(total_weight) / float(moment_index)
    return cg_position

def total_moment(weight, arm):
    return weight * arm

def calculate_lift(cl, rho, velocity, time):
    return 0.5 * cl * rho * velocity**2 * time

def calculate_drag(cd, rho, velocity, time):
    return 0.5 * cl * rho * float(velocity)**2 * time

def calculate_mass(total_weight, g):
    return weight / g

def calculate_acceleration(thrust, drag, total_weight, total_mass):
    return (float(thrust) - float(drag) - float(weight)) / mass

def calculate_velocity(velocity, acceleration, time):
    return float(velocity) + float(acceleration) * float(time)

def calculate_distance(velocity, time):
    return float(velocity) * float(time)

def calculate(event):
    #Range
    fuel_capacity_input = document.querySelector('#fuel_capacity_input')
    fuel_capacity = fuel_capacity_input.value
    fuel_consumption_rate_input = document.querySelector('#fuel_consumption_rate_input')
    fuel_consumption_rate = fuel_consumption_rate_input.value
    true_airspeed_input = document.querySelector('#true_airspeed_input')
    true_airspeed = true_airspeed_input.value
    #Endurance
    fuel_capacity_input = document.querySelector('#fuel_capacity_input')
    fuel_capacity = fuel_capacity_input.value
    fuel_consumption_rate_input = document.querySelector('#fuel_consumption_rate_input')
    fuel_consumption_rate = fuel_consumption_rate_input.value
    #Total Weight
    weight_input = document.querySelector('#weight_input')
    weight = weight_input.value
    payload_input = document.querySelector('#payload_input')
    payload = payload_input.value
    fuel_weight_input = document.querySelector('#fuel_weight_input')
    fuel_weight = fuel_weight_input.value
    #Center of Gravity
    moment_index_input = document.querySelector('#moment_index_input')
    moment_index = moment_index_input.value
    total_weight = calculate_total_weight(payload, fuel_weight, weight)
    #Mass
    g = 9.81
    total_mass = calculate_mass(total_weight, g)
    #Acceleration
    thrust_input = document.querySelector('#thrust_input')
    thrust = thrust_input.value
    drag_input = document.querySelector('#drag_input')
    drag = drag_input.value
    #Velocity
    velocity_input = document.querySelector('#velocity_input')
    velocity = velocity_input.value
    acceleration = calculate_acceleration(thrust, drag, total_weight, total_mass)
    time_input = document.querySelector('#time_input')
    time = time_input.value
    #Distance
    distance = calculate_distance(velocity, time)
    
    #Outputs
    output_div1 = document.querySelector('#output1')
    output_div1.innerText = f"Range: " + str(calculate_range(fuel_capacity, fuel_consumption_rate, true_airspeed)) + " mi" #Range

    output_div2 = document.querySelector('#output2')
    output_div2.innerText = f"Endurance: " + str(calculate_endurance(fuel_capacity, fuel_consumption_rate)) + " hours" #Endurance

    output_div3 = document.querySelector('#output3')
    output_div3.innerText = f"Total Weight: " + str(calculate_total_weight(payload, fuel_weight, weight)) + " lbs" #Total Weight

    output_div4 = document.querySelector('#output4')
    output_div4.innerText = f"Center of Gravity: " + str(calculate_cg_position(moment_index, total_weight)) + " ft" #Center of Gravity

    output_div5 = document.querySelector('#output5')
    output_div5.innerText = f"Mass: " + str(calculate_mass(total_weight, g)) + " lbs" #Mass

    output_div6 = document.querySelector('#output6')
    output_div6.innerText = f"Acceleration: " + str(calculate_acceleration(thrust, drag, total_weight, total_mass)) + " m/s^2" #Acceleration

    output_div7 = document.querySelector('#output7')
    output_div7.innerText = f"Velocity: " + str(calculate_velocity(velocity, acceleration, time)) + " m/s" #Velocity

    output_div8 = document.querySelector('#output8')
    output_div8.innerText = f"Distance: " + str(calculate_distance(velocity, time)) + " mi" #Distance
    


# Values for falcon 9 rocket
fuel_capacity = 901691
fuel_consumption_rate = 1115760
weight = 18000
payload = 50000
fuel_weight = 1210000
mass = 549000
thrust = 7607000
drag = 20.8376
time = 20
velocity = 94.98
true_airspeed = 4150
arm = 2688 # the horizontal distance in inches from the reference datum line to the center of gravity of an object
moment_index = 100
cd = 0.74 # drag coefficient quantifies the resistance of an object relative to its frontal area as it moves through a fluid
acceleration = 5.48
g = 9.81
cl = 1.5 # coefficient of lift is determined by the type of airfoil and angle of attack
rho = 1.12 # rho is used to represent the density of the air at the altitude and conditions where an aircraft is flying
    

range = calculate_range(fuel_capacity, fuel_consumption_rate, true_airspeed)
endurance = calculate_endurance(fuel_capacity, fuel_consumption_rate)
total_weight = calculate_total_weight(payload, fuel_weight, weight)
cg_position = calculate_cg_position(moment_index, total_weight)
lift = calculate_lift(cl, rho, velocity, time)
drag = calculate_drag(cd, rho, velocity, time)
mass = calculate_mass(total_weight, g)
acceleration = calculate_acceleration(thrust, drag, weight, mass)
velocity = calculate_velocity(velocity, acceleration, time)
distance = calculate_distance(velocity, time)
#total_moment = total_moment(weight, arm) # moment is the product of the weight of an object multiplied by its arm
#moment_index = total_moment / 10000


# Displays Performance Calculations
#def pretty_print(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance):
    #print("Performance Calculations:\n")
    #print("Range: {} miles\n".format(range)) # Can also be coded as file.write("Range: " + str(range) + " miles") but isn't simplified. The .format allows the range to be populated in the curly brackets.
    #print("Endurance: {} hours\n".format(endurance))
    #print("Total Weight: {} lbs\n".format(total_weight))
    #print("Center of Gravity: {} ft\n".format(cg_position))
    #print("Lift: {} Newtons\n".format(lift))
    #print("Drag: {} Newtons\n".format(drag))
    #print("Mass: {} lbs\n".format(weight))
    #print("Acceleration: {} m/s^2\n".format(acceleration))
    #print("Velocity: {} m/s\n".format(velocity))
    #print("Distance: {} m\n".format(distance))

#pretty_print(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance)


# To save performance values into txt file, remove comments
#def save_info_to_file(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance, file):
    #file.write("Performance Calculations:\n")
    #file.write("Range: {} miles\n".format(range)) # Can also be coded as file.write("Range: " + str(range) + " miles") but isn't simplified. The .format allows the range to be populated in the curly brackets.
    #file.write("Endurance: {} hours\n".format(endurance))
    #file.write("Total Weight: {} lbs\n".format(total_weight))
    #file.write("Center of Gravity: {} ft\n".format(cg_position))
    #file.write("Lift: {} Newtons\n".format(lift))
    #file.write("Drag: {} Newtons\n".format(drag))
    #file.write("Weight: {} Newtons\n".format(weight))
    #file.write("Acceleration: {} m/s^2\n".format(acceleration))
    #file.write("Velocity: {} m/s\n".format(velocity))
    #file.write("Distance: {} m\n".format(distance))
    #file.close()

#with open("aircraft_performance_analysis.txt", "w") as f:
    #save_info_to_file(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance, file=f) # file=f is another way to introduce a parameter into a function
