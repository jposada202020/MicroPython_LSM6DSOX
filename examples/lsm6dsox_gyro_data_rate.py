# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_lsm6dsox import lsm6dsox

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
lsm = lsm6dsox.LSM6DSOX(i2c)

lsm.gyro_data_rate = lsm6dsox.RATE_104_HZ

while True:
    for gyro_data_rate in lsm6dsox.data_rate_values:
        print("Current Gyro data rate setting: ", lsm.gyro_data_rate)
        for _ in range(3):
            gyrox, gyroy, gyroz = lsm.gyro
            print(f"x:{gyrox:.2f}°/s, y:{gyroy:.2f}°/s, z{gyroz:.2f}°/s")
            print("")
            time.sleep(0.5)
        lsm.gyro_data_rate = gyro_data_rate
