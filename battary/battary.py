from abc import ABC

"""
This is the abstract class for the battary.
  Methods:
    need_service: Returns True if the battary needs service.
    add_years_to_date: Returns the date with the specified number of years added.
"""
class Battary(ABC):
  def need_service(self):
    pass

  def add_years_to_date(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result
