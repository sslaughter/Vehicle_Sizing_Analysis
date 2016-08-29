# Defines the battery class that will hld the data for each battery

class Battery:
    def __int__(self):

        self.brand = ""
        self.capacity = 0 # capacity of battery in mAh
        self.voltage = 0.0 # 3/4S only most likely, possibly to include 6S
        self.weight = 0 # weight of battery in grams
        self.discharge_rating = 0 # "C" rating of battery
        self.current_rating = self.capacity * self.discharge_rating  # current rating, it's the discharge rating multiplied by the capacity
