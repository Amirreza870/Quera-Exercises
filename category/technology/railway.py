class Train:
    
    def __init__(self, 
        last_visited_city: str,
        weight_capacity: float, 
        is_on_trip: bool
    ) -> None:
        self.last_visited_city = last_visited_city
        self.weight_capacity = weight_capacity
        self.is_on_trip = is_on_trip


class Trip:

    all_cities = ('Arak', 'Ardabil', 'Urmia', 'Isfahan', 'Ahvaz', 'Ilam', 'Bojnord', 'Bandar Abbas', 'Bushehr', 'Birjand', 'Tabriz', 'Tehran', 'Khorramabad', 'Rasht', 'Zahedan', 'Zanjan', 'Sari', 'Semnan', 'Sanandaj', 'Shahr-e Kord', 'Shiraz', 'Qazvin', 'Qom', 'Karaj', 'Kermanshah', 'Gorgan', 'Mashhad', 'Hamadan', 'Yasuj', 'Yazd')

    def __init__(
        self,
        origin_city: str, 
        destination_city: str, 
        train: Train
    ) -> None:
        self.train = self.train_validation(train)
        self.destination_city = destination_city
        self.origin_city = self.origin_city_validation(origin_city)
        self.passengers = []
    
    def origin_city_validation(self, origin_city: str):

        if origin_city not in self.all_cities:
            raise Exception("This input is not a verified city")

        elif origin_city == self.destination_city:
            raise Exception("Origin and destination cities can't be the same!")

        elif origin_city != self.train.last_visited_city:
            raise Exception("The train of the trip is not available in the origin city!")

        return origin_city
        
    def train_validation(self, train: Train):

        if not isinstance(train, Train):
            raise Exception("This input is not a train!")

        elif train.is_on_trip:
            raise Exception("This train is not available!")

        return train

    # here implement the magic method
    def __call__(self):
        return self.train.weight_capacity
        


class Passenger:

    def __init__(
        self, 
        fullname: str, 
        load_weight: float
    ) -> None:
        self.fullname = fullname
        self.load_weight = load_weight

    def attend_trip(self, trip: Trip):
        if self.load_weight <= trip.train.weight_capacity:
            trip.passengers.append(self)
        else:
            raise Exception("Heavy load!")

    def cancel_trip(self, trip: Trip):
        if self in trip.passengers:
            trip.passengers.remove(self)
        else:
            raise Exception("This passenger is not attended to this trip!")

    # here implement the magic method
    def __str__(self) -> str:
        return self.fullname
