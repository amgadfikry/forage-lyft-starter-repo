from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battary.spindler_battery import SpindlerBattary
from battary.nubbin_battery import NubbinBattary
from tires.octoprime_tires import OctoprimeTires
from tires.carrigan_tires import CarriganTires


"""
This is a factory class that creates different types of cars.
  Methods:
    create_calliope: Creates a Calliope car.
    create_glissade: Creates a Glissade car.
    create_palindrome: Creates a Palindrome car.
    create_rorschach: Creates a Rorschach car.
    create_thovex: Creates a Thovex car.
"""
class CarFactory:
  @staticmethod
  def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battary = SpindlerBattary(current_date, last_service_date)
    tires = OctoprimeTires(tire_wear_sensors)
    car = Car(engine, battary, tires)
    return car
    
  @staticmethod
  def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battary = SpindlerBattary(current_date, last_service_date)
    tires = CarriganTires(tire_wear_sensors)
    car = Car(engine, battary, tires)
    return car
    
  @staticmethod
  def create_palindrome(current_date, last_service_date, warning_light_is_on, tire_wear_sensors):
    engine = SternmanEngine(warning_light_is_on)
    battery = SpindlerBattary(current_date, last_service_date)
    tires = OctoprimeTires(tire_wear_sensors)
    car = Car(engine, battery, tires)
    return car
  
  @staticmethod
  def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
      engine = WilloughbyEngine(current_mileage, last_service_mileage)
      battery = NubbinBattary(current_date, last_service_date)
      tires = CarriganTires(tire_wear_sensors)
      car = Car(engine, battery, tires)
      return car

  @staticmethod
  def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
      engine = CapuletEngine(current_mileage, last_service_mileage)
      battery = NubbinBattary(current_date, last_service_date)
      tires = OctoprimeTires(tire_wear_sensors)
      car = Car(engine, battery, tires)
      return car