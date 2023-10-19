import math

from solar_system_cartography import envs, utils

class ObjectInOrbit():
    def __init__(self, object_name:str, object_mass:float, semi_major_axis:float, inclination:float, eccentricity:float) -> None:
        self._name = object_name
        self._semi_major_axis = semi_major_axis
        self._inclination = inclination
        self._eccentricity = eccentricity
        self._attraction_mass = envs.SOLAR_MASS # to modify if other center of gravity
        self._mass = object_mass
        self._semi_minor_axis = self.set_semi_minor_axis()
        self._orbital_period = self.set_orbital_period()
        self._orbital_circumference = self.set_orbital_circumference()
        self._perihelion_distance = self.set_perihelion_distance()
        self._perihelion_velocity = self.set_perihelion_velocity()
        self._aphelion_distance = self.set_aphelion_distance()
        self._aphelion_velocity = self.set_aphelion_velocity()
        

    def __repr__(self) -> str:
        return f"""
        ################
        {__class__.__name__} : {self._name}
        ################

        # ORBITAL CHARACTERISTICS
        semi major axis : {self._semi_major_axis} AU
        semi minor axis : {self._semi_minor_axis} AU
        inclination : {self._inclination}°
        eccentricity : {self._eccentricity}
        period : {self._orbital_period} days
        circumference : {self._orbital_circumference} m
        distance at perihelion : {self._perihelion_distance} AU
        velocity at perihelion : {self._perihelion_velocity} m/s
        distance at aphelion : {self._aphelion_distance} AU
        velocity at aphelion : {self._aphelion_velocity} m/s

        # PHYSICAL CHARACTERISTICS
        mass : {self._mass} kg
            """
    
    def get_name(self) ->str:
        return self._name
    
    def get_semi_major_axis(self) ->float:
        return self._semi_major_axis
    
    def get_inclination(self) ->float:
        return self._inclination
    
    def get_eccentricity(self) ->float:
        return self._eccentricity
    
    def get_orbital_period(self) ->float:
        return self._orbital_period
    
    def set_orbital_period(self) ->float:
        """
        Calculates the time in days that it takes for a star to make a
        complete revolution around the Sun from its distance from the Sun.
        """
        # Using Kepler's law to calculate the orbital period (T)
        orbital_period = 2 * math.pi * math.sqrt((utils.convert_au_to_meters(self._semi_major_axis)**3) / (envs.G * self._attraction_mass))
        
        # Conversion to days
        return orbital_period / (60 * 60 * 24)

    def get_semi_minor_axis(self) ->float:
        return self._semi_minor_axis
    
    def set_semi_minor_axis(self) ->float:
        """Calculates the semi minor axis of an ellipse.

        Returns:
            float: The semi minor axis of the ellipse
        """
        return self._semi_major_axis * math.sqrt(1 - self._eccentricity ** 2)

    def get_perihelion_distance(self) ->float:
        return self._perihelion_distance
    
    def set_perihelion_distance(self) ->float:
        return self._semi_major_axis * (1 - self._eccentricity)

    def get_perihelion_velocity(self) ->float:
        return self._perihelion_velocity
    
    def set_perihelion_velocity(self) ->float:
        """Calculate the speed of an object at perihelion around the Sun

        Returns:
            float: The velocity in meters
        """
        return math.sqrt(envs.G * (self._attraction_mass + self._mass) * (2 / utils.convert_au_to_meters(self._perihelion_distance) - 1 / utils.convert_au_to_meters(self._semi_major_axis)))

    def get_aphelion_distance(self) ->float:
        return self._aphelion_distance
    
    def set_aphelion_distance(self) ->float:
        return self._semi_major_axis * (1 + self._eccentricity)
    
    def get_aphelion_velocity(self) ->float:
        return self._aphelion_velocity
    
    def set_aphelion_velocity(self) ->float:
        """Calculate the speed of an object at aphelion around the Sun

        Returns:
            float: The velocity in meters
        """
        return math.sqrt(envs.G * (self._attraction_mass + self._mass) * (2 / utils.convert_au_to_meters(self._aphelion_distance) - 1 / utils.convert_au_to_meters(self._semi_major_axis)))

    def get_orbital_circumference(self) ->float:
        return self._orbital_circumference
    
    def set_orbital_circumference(self) ->float:
        return 2 * math.pi * (self._semi_major_axis * envs.AU) # in meters
    
    def get_circumference_percentage(self, radius:float, time:int) ->float:
        # time in days
        # radius = perihelion distance at first

        # Kepler's law
        orbital_speed = (2 * math.pi * radius) / self._orbital_period

        # percentage of covered distance
        return self._orbital_circumference / 100 * (orbital_speed * time)
    
if __name__ == "__main__":
    # print(get_semi_minor_axis(30.0699, 0.00859))
    # print(get_orbital_period(convert_au_to_meters(0.38709808989279954)))

    def get_perihelion():
        inclinaison_degrees = 162.238  # Inclinaison de l'orbite en degrés
        longitude_du_noeud_ascendant_degrees = 58  # Longitude du nœud ascendant en degrés

        # Conversion des angles en radians
        inclinaison_radians = math.radians(inclinaison_degrees)
        longitude_du_noeud_ascendant_radians = math.radians(longitude_du_noeud_ascendant_degrees)

        # Calcul de l'argument du périhélie (ω) en radians
        argument_du_perihelie_radians = math.atan2(-math.cos(inclinaison_radians) * math.sin(longitude_du_noeud_ascendant_radians), math.cos(longitude_du_noeud_ascendant_radians))

        # Conversion de l'angle résultant en degrés
        argument_du_perihelie_degrees = math.degrees(argument_du_perihelie_radians)

        return argument_du_perihelie_degrees
    
    object_name = "Mercury"