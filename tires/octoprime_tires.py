from tires.tires import Tires

class OctoprimeTires(Tires):
  def __init__(self, tire_wear_sensors):
    self.tire_wear_sensors = tire_wear_sensors

  def needs_service(self):
    high_wear = sum(self.tire_wear_sensors)
    return high_wear >= 3