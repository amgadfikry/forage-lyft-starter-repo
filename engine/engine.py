from abc import ABC

"""
Engine class is an abstract class that defines the interface for all engine types.
"""
class Engine(ABC):
  def needs_service(self):
    pass