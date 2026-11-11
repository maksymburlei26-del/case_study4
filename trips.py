from bikes import Station, Bike
from clients import Client


class RentalSystem:
    def __init__(self):
        self.total_revenue = 0

    def start_rent(self, station: Station):
        return station.remove_bike()

    def calculate_cost(self, bike: Bike, minutes: int):
        return bike.get_rate() * minutes

    def finish_rent(self, client: Client, bike: Bike, end_station: Station, minutes: int):
        cost = self.calculate_cost(bike, minutes)

        if client.withdraw(cost):
            end_station.add_bike(bike)
            self.total_revenue += cost
            return True, "Успішна поїздка", cost
        else:
            end_station.add_bike(bike)
            return False, "Недостатньо коштів на балансі", cost

    def get_total_revenue(self):
        return self.total_revenue