from battary.battary import Battary

"""
This is the NubbinBattary class.
  Attributes:
    current_date: The current date.
    last_service_date: The date when the battary was last serviced.
  Methods:
    need_service: Returns True if the battary needs service.
"""
class NubbinBattary(Battary):
  def __init__(self, current_date, last_service_date):
    self.current_date = current_date
    self.last_service_date = last_service_date

  def need_service(self):
    date_need_to_serve = Battary.add_years_to_date(self.last_service_date, 4)
    return self.current_date > date_need_to_serve