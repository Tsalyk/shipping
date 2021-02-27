class Vehicle:
    """
    Represents info about vehicles
    """

    def __init__(self, vehicleNo: int):
        self.vehicleNo = vehicleNo
        self.isAvailable = True


class Location:
    """
    Represents info about a location,
    where items should be ordered
    """

    def __init__(self, city: str, postoffice: int):
        self.city = city
        self.postoffice = postoffice


class Item:
    """
    Represents info about a delivering item
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price