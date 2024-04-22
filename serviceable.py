from abc import ABC, abstractmethod

"""
This is the Serviceable class that will be used to create the Car class.
  Methods:
    needs_service: Abstract method that will be implemented in the Car class.
"""
class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
