import serial
import pynmea2
from metaclasses.Singleton import SingletonMetaClass


class GPS(metaclass=SingletonMetaClass):
    __PORT = '/dev/ttyAMA0'
    __SERIAL = serial.Serial(__PORT, baudrate=9600, timeout=0.5)

    def read_coordinates(self):
        n_data = "11231231231"
        while n_data[0:6] != '$GPRMC':
            new_data = self.__SERIAL.readline()
            n_data = new_data.decode('latin-1')
        new_msg = pynmea2.parse(n_data)
        print(n_data)
        lat = round(new_msg.latitude, 5)
        lng = round(new_msg.longitude, 5)
        return {
            "latitude": lat,
            "longitude": lng
        }

    def __del__(self):
        self.__SERIAL.close()
