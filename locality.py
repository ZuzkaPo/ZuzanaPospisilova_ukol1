from math import ceil
from abc import ABC, abstractmethod
from enum import Enum

#Enum trida pro typy pozemku
class Estate_type(Enum):
    GARDEN = (2, "Zahrada")
    FORREST = (0.35, "Les")
    LAND = (0.85, "Zemedelsky pozemek")
    BUILDING_SITE = (9, "Stavebni pozemek")
    
    def __init__(self, coefficient, description):
        self.coefficient = coefficient
        self.description = description
        
#trida pro urceni lokality
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient
        
#abstraktni trida od ktere budou dedit pozemky a nemovitosti
class Property(ABC):
    @abstractmethod      
    def calculate_tax(self):
        pass

#trida pro pozemky   
class Estate(Property):
    def __init__(self, locality, estate_type: Estate_type, area):
        self.locality = locality
        self.estate_type = estate_type
        self.area =area
        
    def calculate_tax(self):
        return ceil(self.estate_type.coefficient * self.area * self.locality.locality_coefficient)
    
    def __str__(self):
        return f"{self.estate_type.description}, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metru ctverecnich, dan {self.calculate_tax()}"

#trida pro nemovitosti     
class Residence(Property):
    def __init__(self, locality, area, comercial):
        self.locality = locality
        self.area = area
        self.comercial = comercial
        
    def calculate_tax(self):
        tax = ceil(self.area * 15 * self.locality.locality_coefficient)
        if self.comercial:
            return tax * 2
        else:
            return tax
        
    def __str__(self):
        typ = "Nekomercni nemovitost"
        if self.comercial:
            typ = "Komercni nemovitost"
            
        return f"{typ}, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metru ctverecnich, dan {self.calculate_tax()}"

#Trida pro danove priznani    
class TaxReport:
    def __init__(self, name, property_list):
        self.name = name
        self.property_list = property_list
        
    def add_property(self, property):
        self.property_list.append(property)
        
    def calculate_tax(self):
        tax = 0
        for i in self.property_list:
            tax += i.calculate_tax()
        return tax
    def __str__(self):
        return f"{self.name} ma {len(self.property_list)} nemovitosti a dan z nemovitosti cini {self.calculate_tax()} Kc." 