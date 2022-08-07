# modified from official Waveshare RPi Sense Hat (B) example zip folder
# example download instructions can be found here: https://www.waveshare.com/wiki/Sense_HAT_(B)

#!/usr/bin/python
# -*- coding:utf-8 -*-
import ctypes

class SHTC3:
    def __init__(self):
        self.dll = ctypes.CDLL("./SHTC3.so")
        init = self.dll.init
        init.restype = ctypes.c_int
        init.argtypes = [ctypes.c_void_p]
        init(None)

    def SHTC3_Read_Temperature(self):
        temperature = self.dll.SHTC3_Read_TH
        temperature.restype = ctypes.c_float
        temperature.argtypes = [ctypes.c_void_p]
        return temperature(None)

    def SHTC3_Read_Humidity(self):
        humidity = self.dll.SHTC3_Read_RH
        humidity.restype = ctypes.c_float
        humidity.argtypes = [ctypes.c_void_p]
        return humidity(None)


# if __name__ == "__main__":
#     shtc3 = SHTC3()
#     while True:
#         print('Temperature = %6.2f°C , Humidity = %6.2f%%' % (shtc3.SHTC3_Read_Temperature(), shtc3.SHTC3_Read_Humidity()))

class TH(SHTC3):
    """
    TH = Temperature and Humidity
    """

    def __init__(self):
        super().__init__()

    @property
    def temperature(self):
        """
        Temperature in Celcius
        """
        return self.SHTC3_Read_Temperature()

    @property
    def humidity(self):
        """
        Humidity as a percentage
        """
        return self.SHTC3_Read_Humidity()