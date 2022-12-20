import itertools


class Room:
    id_obj = itertools.count()

    """
    This class represents a room, which contains of a name and a list of temperatures.
    :param int id: The id of the room.
    :param list temperatures: A list of numbers containing temperatures.
    """

    def __init__(self, temperatures=None):
        if temperatures is None:
            temperatures = []
        self.id = next(Room.id_obj)
        self.temperatures = temperatures

    def average(self):
        """
        Calculate the average of the subject with consideration of the weighing and print it out.
        If there are no grades, it will print out an error message.
        """
        if not self.temperatures:
            print("Keine Temperaturen vorhanden!")
            return

        total = 0
        for t in self.temperatures:
            total = total + t

        return round(total / len(self.temperatures), 3)

    def add_temperature(self, temperature):
        """
        Append a temperature to the temperature's list.
        """
        self.temperatures.append(temperature)

    def evaluation(self):
        avg = self.average()
        if avg:
            if avg < 19:
                return 'badge-blue'
            elif 19 <= avg <= 21:
                return 'badge-green'
            elif 21 <= avg <= 23:
                return 'badge-orange'
            else:
                return 'badge-red'
