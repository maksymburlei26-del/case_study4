class Bicycle:
    def __init__(self, bike_id, bike_type):
        self.bike_id = bike_id
        self.bike_type = bike_type


class Station:
    def __init__(self, name):
        self.name = name
        self.bikes = []

    def add_bike(self, bike):
        self.bikes.append(bike)

    def remove_bike(self, bike_type):
        for bike in self.bikes:
            if bike.bike_type == bike_type:
                self.bikes.remove(bike)
                return bike
        return None

    def get_bikes_count(self):
        counts = {'звичайний': 0, 'електричний': 0}
        for bike in self.bikes:
            if bike.bike_type in counts:
                counts[bike.bike_type] += 1
        return counts