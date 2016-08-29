"""
This is the main file that will perform the data analysis.
it will:
    - read all of the motor data from the motor files. Will be within motors directory
        - create a list of motor/prop combinations with motor data
        - populate motor class data for each one w/ interpolation stuff, etc

Pseudocode:

Read all files in motor directory
Populate list of instances of motor class - will include prop data
Populate list of batteries from battery.txt file
Populate ist of escs from esc.txt - probably optional

for each motor/prop:
    for each battery:
        for each esc:
            for each configuration - quadcopter, hexacopter, x-8, need to figure out minimum vehicle size for
            each configuration w/ prop size
                calculate vehicle weight
                calculate resulting flight time (find required throttle, resulting current, battery capacity)


"""

import Motors
import Battery
import os


frame_weight = 30  # percentage of AUW attributed to the frame
payload_weight = 600 # weight of payload in grams
battery_usage = .80 # percentage of usable battery capacity


dir_path = os.getcwd()
motor_path = dir_path + "/Motors"
motor_files = os.listdir(motor_path)

configurations = []
batteries = []
escs = []





for motor in motor_files:
    temp_motor_file = open(motor, 'r')
    first_line = temp_motor_file.readline()
    motor_params = first_line.split(",")

    temp_motor = Motors.Motor(motor_params[0], motor_params[1], motor_params[2])

    line_is_prop = True

    for line in temp_motor_file:
        line_list = line.split(",")

        if line_list[0] == "A":
            temp_motor_prop = Motors.Motor_Prop(int(line_list[1]), int(line_list[2]))
            line_is_prop = False

        new_temp_line = ""
        while new_temp_line != "B":
            new_temp_line = temp_motor_file.readline()
            motor_data = new_temp_line.split(",")

            temp_motor_prop.throttle_percentage.append(int(motor_data[0]))
            temp_motor_prop.throttle_thrust.append(int(motor_data[1]))
            temp_motor_prop.throttle_current.append(int(motor_data[2]))

        temp_motor.prop_list.append(temp_motor_prop)
        line_is_prop = True


if __name__ == "__main__":
    #execute only if run asa script
    main()