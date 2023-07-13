# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_lsm6dsox import lsm6dsox

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
lsm = lsm6dsox.LSM6DSOX(i2c)

lsm.acceleration_range = lsm6dsox.RANGE_8G

while True:
    for acceleration_range in lsm6dsox.acceleration_range_values:
        print("Current Acceleration range setting: ", lsm.acceleration_range)
        for _ in range(3):
            accx, accy, accz = lsm.acceleration
            print(f"x:{accx:.2f}m/s2, y:{accy:.2f}m/s2, z{accz:.2f}m/s2")
            print()
            time.sleep(0.5)
        lsm.acceleration_range = acceleration_range
