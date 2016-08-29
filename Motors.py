"""
This will define the motor class which will hold pertinent data on a motor.

It will also likely include the propeller class as they're tied to the motors anyway.
"""



class Motor:
    def __int__(self, brand, model, kv):

        self.brand = brand
        self.model = model
        self.kv = kv

        self.prop_list = []






class Motor_Prop:

    def __init__(self, size, pitch):

        self.prop_size = size
        self.prop_pitch = pitch

        self.throttle_percentage = []
        self.throttle_thrust = []
        self.throttle_current = []



    def function_interpolation(self):
        pass







