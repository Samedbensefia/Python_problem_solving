class Vehicle:
    def __init__(self, License_plate, Brand, Weight):
        self.License_plate = License_plate
        self.Brand = Brand
        self.Weight = Weight
    
    def describe(self):
        pass
    
class Car(Vehicle):
    def __init__(self, License_plate, Brand, Weight, seats):
        super().__init__(License_plate, Brand, Weight,seats)
        self.seats = seats

class Track(Vehicle):
    def __init__(self, License_plate, Brand, Weight, load_capacity):
        super().__init__(License_plate, Brand, Weight, load_capacity)
        self.load_capacity = load_capacity
    def accelerate():
        pass


class Park:
    
    def __init__(self):
        self.vehicles = list[Vehicle]
        
    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
        
    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)
        
    def list_vehicles(self):
        '''
        returns the list of vehicles
        '''
        return [ Vehicle(vehicle).describe() for vehicle in self.vehicles ]