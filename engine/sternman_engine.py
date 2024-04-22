from engine.engine import Engine

"""
this is a simple class that represents a Sternman engine inherited from the Engine class.
  Attributes:
    warning_light_is_on: A boolean value that indicates if the warning light is on.
  Methods:
    engine_should_be_serviced: Returns True if the warning light is on.
"""
class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
