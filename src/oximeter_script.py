import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from scipy.signal import find_peaks
import threading
import time

plt.ion()

fig, ax = plt.subplots()

start_time = time.time()
dataArray_red = np.array([])
dataArray_ir = np.array([])

peaks_1 = []
peaks_2 = []

values = []

def detect_oxygen(red_data, ir_data, sampling_rate):
    ir_dc = np.mean(red_data)
    red_dc = np.mean(red_data)

    ir_ac = np.max(ir_data) - np.min(ir_data)
    red_ac = np.max(red_data) - np.min(red_data)

    red_ac_dc_ration = red_ac / red_dc
    ir_ac_dc_ration = ir_ac / ir_dc
    R = red_ac_dc_ration / ir_ac_dc_ration

    SpO2 = round((1.6 *R**2) + (-34.5*R) + 122.2)
    if SpO2 >= 100:
        print(SpO2, "%... SpO2 Exceeded 100, O_o")
    else:
        print("SpO2: ", SpO2, "%")
    return SpO2

def detect_heart_rate(sensor_data, sampling_rate):

    peaks, _ = find_peaks(-sensor_data, prominence=50 )
    print(peaks)

    peak_distances = np.diff(peaks)
    heart_rate = (60 * sampling_rate / np.mean(peak_distances))
    return heart_rate


def sendData(Data):
    parts = Data.split()
    ir, red = int(float(parts[0])), int(float((parts[1])))

    global start_time
    global dataArray_red
    global dataArray_ir

    if (time.time() - start_time) < 8:
        dataArray_red = np.append(dataArray_red, red)
        dataArray_ir = np.append(dataArray_ir, ir)
        time.sleep(0.0025)
    else:
        sample_rate = len(dataArray_red) / 8
        heart_rate = detect_heart_rate(dataArray_red, sample_rate)
        print("\nBPM: ", round(heart_rate, 0))
        oxygen = detect_oxygen(dataArray_red, dataArray_ir, sample_rate)
        start_time = time.time()
        dataArray_red = np.array([])
        dataArray_ir = np.array([])
        peaks_1 = []
        peaks_2 = []

    global values


    values.append(-red)
    values = values[-180:]

    x = np.arange(len(values))

    # Plotting
    plt.plot(x, values)
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Plot Inside While Loop')

    plt.pause(0.0001)
    plt.clf()
    # # time_between_samples = time.time() - cycle_start
