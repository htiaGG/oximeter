import serial
import importlib
import time
import keyboard
import threading
import matplotlib.pyplot as plt

def open_serial_port(port, baudrate):
    try:
        ser = serial.Serial(port, baudrate)
        return ser
    except Exception as e:
        print("Error opening serial port:", e)
        return None

data = None

def reload_script():
    try:
        importlib.reload(oximeter_script)
        print("Script reloaded successfully")
    except Exception as e:
        print("Error reloading script:", e)

ser = open_serial_port('COM7', 9600)  # Replace 'COM7' with the appropriate port name

def read_and_send():
    while True:
        global data
        # if data == None:
        #     continue
        data = ser.readline().decode().strip()

thread = threading.Thread(target=read_and_send)
thread.start()

paused = False

if ser:
    try:
        # Import the script module
        import oximeter_script

        print("Press Ctrl+C to stop")
        while True:
            if (paused != True):
                oximeter_script.sendData(data)
            else:
                time.sleep(0.1)

            if keyboard.is_pressed('ctrl+5'):
                reload_script()
                plt.close('all')
            if keyboard.is_pressed('ctrl+4'):
                paused = True
            if keyboard.is_pressed('ctrl+3'):
                paused = False

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()
