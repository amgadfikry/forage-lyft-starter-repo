from engine.engine import Engine

"""
this is a simple class that represents a Willoughby engine inherited from the Engine class.
  Attributes:
    current_mileage: The current mileage of the engine.
    last_service_mileage: The mileage when the engine was last serviced.
  Methods:
    engine_should_be_serviced: Returns True if the engine mileage is greater than 60000 miles since the last service.
"""
class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000
