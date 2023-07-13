# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_lsm6dsox import lsm6dsox

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
lsm = lsm6dsox.LSM6DSOX(i2c)

lsm.high_pass_filter = lsm6dsox.HPF_DIV400

while True:
    for high_pass_filter in lsm6dsox.high_pass_filter_values:
        print("Current High pass filter setting: ", lsm.high_pass_filter)
        for _ in range(10):
            accx, accy, accz = lsm.acceleration
            print(f"x:{accx:.2f}m/s2, y:{accy:.2f}m/s2, z{accz:.2f}m/s2")
            print()
            time.sleep(0.5)
        lsm.high_pass_filter = high_pass_filter
