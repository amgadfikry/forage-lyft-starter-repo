from serviceable import Serviceable

"""
This is a simple class that represents a car. It has an engine and a battery.
  Attributes:
    engine: An instance of the Engine class.
    battery: An instance of the Battery class.
  Methods:
    needs_service: Returns True if either the engine or the battery needs service.
"""
class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.Battery = battery
        self.tires = tires

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
