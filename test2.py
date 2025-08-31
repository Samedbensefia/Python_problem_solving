class Vehicle:
    
    def __init__(self, License_plate, Brand, Weight) -> None:
        self.License_plate = License_plate
        self.Brand = Brand
        self.Weight = Weight
    
    def describe(self) -> str:
        """
        Returns a string describing the vehicle with its brand, license plate, and weight.
        """
        return f" Brand: {self.Brand} -  License Plate: {self.License_plate} - Weight: {self.Weight}"
    
    def set_License_plate(self):
        self.License_plate = input("Enter license plate: ")
    
    def get_License_plate(self):
        return f"License plate: {self.License_plate}"
        
    
    
    
class Car(Vehicle):
    def __init__(self, License_plate, Brand, Weight, seats):
        super().__init__(License_plate, Brand, Weight)
        self.seats = seats
    
    def describe(self):
        """
        Returns a string describing the object, including the base description and the number of seats.
        extends the describe method of the Vehicle class to include number of seats
        """
        base_description = super().describe()
        return f"{base_description} - Seats: {self.seats}" 



class Track(Vehicle):
    def __init__(self, License_plate, Brand, Weight, load_capacity):
        super().__init__(License_plate, Brand, Weight)
        self.load_capacity = load_capacity
    
    def describe(self):
        """
        extends the describe method of the Vehicle class to include load capacity
        """
        base_description = super().describe()
        return f"{base_description} - Load Capacity: {self.load_capacity}" 




class Park:
    
    def __init__(self):
        """
        initilizes the park with an empty list of vehicles
        """
        self.vehicles = []
        
    def add_vehicle(self, vehicle: Vehicle) -> None:
        """
        adds a vehicle to the park 
        """
        self.vehicles.append(vehicle)
        
    def remove_vehicle(self, vehicle: Vehicle) -> None:
        """
        removes a vehicle from the park
        """
        self.vehicles.remove(vehicle)
        
    def list_vehicles(self) -> list[str]:
        '''
        returns the list of vehicles in the park
        as a list of strings with the description of each vehicle
        '''
        return [ vehicle.describe() for vehicle in self.vehicles ]
        
    

track1 = Track( "2019-32-ORA" , "ISUZI", "12T" ,"3" )
car1 = Car("2020-12-BBM" , "BMW" , "4T" , "5")
car2 = Car("1999-58-EBH" , "MERCEDES" , "1T" , "2")
track2 = Track("2000-43-ALG" , "FIAT" , "12T" , "500KG")


park = Park()


park.add_vehicle(track1)
park.add_vehicle(car2)
for v in park.list_vehicles():
    print(v)

