# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_lsm6dsox import lsm6dsox

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
lsm = lsm6dsox.LSM6DSOX(i2c)

# The sensor seems to return strange values doing this example
# Not sure why. Work left for the reader


data_rate_values = (
    lsm6dsox.RATE_104_HZ,
    lsm6dsox.RATE_208_HZ,
    lsm6dsox.RATE_416_HZ,
    lsm6dsox.RATE_833_HZ,
    lsm6dsox.RATE_1_66K_HZ,
    lsm6dsox.RATE_3_33K_HZ,
    lsm6dsox.RATE_6_66K_HZ,
)

lsm.acceleration_data_rate = lsm6dsox.RATE_104_HZ


while True:
    for acceleration_data_rate in data_rate_values:
        print("Current Acceleration data rate setting: ", lsm.acceleration_data_rate)
        for _ in range(3):
            accx, accy, accz = lsm.acceleration
            print(f"x:{accx:.2f}m/s2, y:{accy:.2f}m/s2, z{accz:.2f}m/s2")
            print()
            time.sleep(0.5)
        lsm.acceleration_data_rate = acceleration_data_rate
