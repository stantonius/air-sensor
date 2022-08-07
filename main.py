from pressure import Pressure
from temp_humidity import TH
import time

if __name__ == "__main__":
    press = Pressure()
    th = TH()
    while True:
        time.sleep(1)
        print(press.measurement)
        print(th.temperature)
        print(th.humidity)
