
class Bus:
    def __init__(self, route, destination):
        self.route_number = route
        self.destination = destination
        self.passengers = []       

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, picked_up):
        self.passengers.append(picked_up)

    def drop_off(self, passenger_2):
        self.passengers.remove(passenger_2)

    def empty_bus(self):
        self.passengers.clear()

    