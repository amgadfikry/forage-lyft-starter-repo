from tires.tires import Tires

class CarriganTires(Tires):
  def __init__(self, tire_wear_sensors):
    self.tire_wear_sensors = tire_wear_sensors

  def needs_service(self):
    high_wear = any([sensor >= 0.9 for sensor in self.tire_wear_sensors])
    return high_wear
