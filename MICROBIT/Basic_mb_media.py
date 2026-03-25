from microbit import *
def main():
    Max = 15
    i = 1
    accel_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    accel_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    accel_z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while True:
        if i < Max:
            accel_x[Max-i] = accel_x[Max-i-1]
            accel_y[Max-i] = accel_y[Max-i-1]
            accel_z[Max-i] = accel_z[Max-i-1]
            i = i + 1
        else:
            i = 1
            accel_x[0] = accelerometer.get_x()
            accel_y[0] = accelerometer.get_y()
            accel_z[0] = accelerometer.get_z()
            sleep(200)
            tx = 0
            ty = 0
            tz = 0
            suma_x = 0
            suma_y = 0
            suma_z = 0
            media_x = 0
            media_y = 0
            media_z = 0
            for tx in accel_x:
                suma_x = suma_x + tx
            for ty in accel_y:
                suma_y = suma_y + ty
            for tz in accel_z:
                suma_z = suma_z + tz
            media_x = suma_x / Max
            media_y = suma_y / Max
            media_z = suma_z / Max
            #print(accel_x, accel_y, accel_z)
            print( (media_x, media_y, media_z) )
if __name__ == "__main__":
    main()