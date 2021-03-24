#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:00:24 2021

@author: benjaminlow
"""

# LR3_Question_8


import numpy as np
import matplotlib.pyplot as plt
import Lab3Functions as l3f
import EMGFunctions as emgf
import pickle 
import scipy as sp

column_names = ['emg', 't']


# put three files all together
weights, mvc, fatigue = l3f.import_data('\t')

# removing the mean
mvc_emgcorrectmean = emgf.remove_mean(mvc.emg, mvc.t/1000)
weights_emg_correctmean = emgf.remove_mean(weights.emg, weights.t/1000)

# pre-process of EMG data
mvc_emg_filtered, mvc_emg_envelope = emgf.alltogether(mvc.t/1000, mvc_emgcorrectmean, low_pass=2, sfreq=1000, high_band=20, low_band=450 )
weights_emg_filtered, weights_emg_envelope = emgf.alltogether(weights.t/1000, weights_emg_correctmean, low_pass=2, sfreq=1000, high_band=20, low_band=450 )


# Burst (start & end)
mvc_start = pickle.load(open("mvc_start.txt", "rb")) 
mvc_end = pickle.load(open("mvc_end.txt", "rb")) 
weights_start = pickle.load(open("weights_start.txt", "rb")) 
weights_end = pickle.load(open("weights_end.txt", "rb")) 


# Calculate mean MVC
mean_mvc1 = np.mean(mvc_emg_envelope[mvc_start[0]:mvc_end[0]])
mean_mvc2 = np.mean(mvc_emg_envelope[mvc_start[1]:mvc_end[1]])
mean_mvc3 = np.mean(mvc_emg_envelope[mvc_start[2]:mvc_end[2]])

mean_all_mvc = np.mean([mean_mvc1, mean_mvc2, mean_mvc3])

# Calculate mean Weights
mean_weights1 = np.mean(weights_emg_envelope[weights_start[0]:weights_end[0]])
mean_weights2 = np.mean(weights_emg_envelope[weights_start[1]:weights_end[1]])
mean_weights3 = np.mean(weights_emg_envelope[weights_start[2]:weights_end[2]])

# Percentage to MVC
weight_25_emg = mean_weights1/mean_all_mvc
weight_50_emg = mean_weights2/mean_all_mvc
weight_75_emg = mean_weights3/mean_all_mvc

# Plot Relative Muscle Activation

x = [13, 25, 40]

y = [weight_25_emg, weight_50_emg, weight_75_emg]

plt.figure()
plt.plot(x, y, marker='o')
plt.title('Question 7_Relative Muscle Activation')
plt.xlabel('Weight/Resistence (lb)')
plt.ylabel('% MVC')

#9
weights, mvc, fatigue = l3f.import_data('\t')

fatigue_emgcorrectmean = emgf.remove_mean(fatigue.emg, fatigue.t/1000)

fatigue_emg_filtered, fatigue_emg_envelope = emgf.alltogether(fatigue.t/1000, fatigue_emgcorrectmean, low_pass=5, sfreq=1000, high_band=20, low_band=450)

# mvc_start, mvc_end, weights_start, weights_end, fatigue_start, fatigue_end = l3f. get_bursts(
    # mvc_emg_filtered, weights_emg_filtered, fatigue_emg_filtered)

# pickle.dump(fatigue_start, open("fatigue_start.txt", "wb"))
fatigue_start = pickle.load(open("fatigue_start.txt", "rb"))
# pickle.dump(fatigue_end, open("fatigue_end.txt", "wb"))
fatigue_end = pickle.load(open("fatigue_end.txt", "rb"))

 # Sampling Frequency is about 400 Hz.~~~~

  #Question 9

    #Fatigue 1

array1 = fatigue_emg_filtered[fatigue_start[0]:fatigue_end[0]]
arraystart1 = array1[0:200]
arraymid1 = array1[1300:1500]
arrayend1 = array1[2400:2600]

    #Fatigue 1 Start
    
power, frequencies = l3f.get_power(arraystart1, 400)
b2, a2 = sp.signal.butter(4, 0.08, btype='lowpass')
power_filt1 = sp.signal.filtfilt(b2, a2, power)
power_med1 = np.median(power_filt1)

plt.figure()
plt.plot(frequencies, power, label = 'Raw Frequency')
plt.plot(frequencies, power_filt1, color = 'red', label = 'Filtered Frequency')
plt.axvline(power_med1, color = 'black', label = 'Median')
plt.title('Raw and Filtered Power Spectrum with Meadian Line')
plt.ylabel('Power (a.u.)')
plt.xlabel('Frequency (Hz)')
plt.legend()

    # Fatigue 1 Middle

power, frequencies = l3f.get_power(arraymid1, 400)
b2, a2 = sp.signal.butter(4, 0.08, btype='lowpass')
power_filt2 = sp.signal.filtfilt(b2, a2, power)
power_med2 = np.median(power_filt2)

plt.figure()
plt.plot(frequencies, power)
plt.plot(frequencies, power_filt2, color = 'red')
plt.axvline(power_med2, color = 'red')
plt.title('Raw and Filtered Power Spectrum with Meadian Line')
plt.ylabel('Power (a.u.)')
plt.xlabel('Frequency (Hz)')

    #Fatigue 1 End

power, frequencies = l3f.get_power(arrayend1, 400)
b2, a2 = sp.signal.butter(4, 0.08, btype='lowpass')
power_filt3 = sp.signal.filtfilt(b2, a2, power)
power_med3 = np.median(power_filt3)

plt.figure()
plt.plot(frequencies, power)
plt.plot(frequencies, power_filt3, color = 'red')
plt.axvline(power_med3, color = 'red')
plt.title('Raw and Filtered Power Spectrum with Meadian Line')
plt.ylabel('Power (a.u.)')
plt.xlabel('Frequency (Hz)')

    #Fatigue 2

array2 = fatigue_emg_filtered[fatigue_start[1]:fatigue_end[1]]
arraystart2 = array2[0:200]
arraymid2 = array2[1500:1700]
arrayend2 = array2[2800:3000]

    #Fatigue 2 Start
    
power, frequencies = l3f.get_power(arraystart2, 400)
b2, a2 = sp.signal.butter(4, 0.08, btype='lowpass')
power_filt1 = sp.signal.filtfilt(b2, a2, power)
power_med4 = np.median(power_filt1)

plt.figure()
plt.plot(frequencies, power)
plt.plot(frequencies, power_filt1, color = 'red')
plt.axvline(power_med4, color = 'red')
plt.title('Raw and Filtered Power Spectrum with Meadian Line')
plt.ylabel('Power (a.u.)')
plt.xlabel('Frequency (Hz)')

     # Fatigue 2 Middle

power, frequencies = l3f.get_power(arraymid2, 400)
b2, a2 = sp.signal.butter(4, 0.08, btype='lowpass')
power_filt2 = sp.signal.filtfilt(b2, a2, power)
power_med5 = np.median(power_filt2)

plt.figure()
plt.plot(frequencies, power)
plt.plot(frequencies, power_filt2, color = 'red')
plt.axvline(power_med5, color = 'red')
plt.title('Raw and Filtered Power Spectrum with Meadian Line')
plt.ylabel('Power (a.u.)')
plt.xlabel('Frequency (Hz)')

    #Fatigue 2 End

power, frequencies = l3f.get_power(arrayend2, 400)
b2, a2 = sp.signal.butter(4, 0.08, btype='lowpass')
power_filt3 = sp.signal.filtfilt(b2, a2, power)
power_med6 = np.median(power_filt3)

plt.figure()
plt.plot(frequencies, power)
plt.plot(frequencies, power_filt3, color = 'red')
plt.axvline(power_med6, color = 'red')
plt.title('Raw and Filtered Power Spectrum with Meadian Line')
plt.ylabel('Power (a.u.)')
plt.xlabel('Frequency (Hz)')
    
    #Fatigue 3

array3 = fatigue_emg_filtered[fatigue_start[2]:fatigue_end[2]]
arraystart3 = array3[0:200]
arraymid3 = array3[1400:1600]
arrayend3 = array3[2600:2800]

    #Fatigue 3 Start
    
power, frequencies = l3f.get_power(arraystart3, 400)
b2, a2 = sp.signal.butter(4, 0.08, btype='lowpass')
power_filt1 = sp.signal.filtfilt(b2, a2, power)
power_med7 = np.median(power_filt1)

plt.figure()
plt.plot(frequencies, power)
plt.plot(frequencies, power_filt1, color = 'red')
plt.axvline(power_med7, color = 'red')
plt.title('Raw and Filtered Power Spectrum with Meadian Line')
plt.ylabel('Power (a.u.)')
plt.xlabel('Frequency (Hz)')

     # Fatigue 3 Middle

power, frequencies = l3f.get_power(arraymid3, 400)
b2, a2 = sp.signal.butter(4, 0.08, btype='lowpass')
power_filt2 = sp.signal.filtfilt(b2, a2, power)
power_med8 = np.median(power_filt2)

plt.figure()
plt.plot(frequencies, power)
plt.plot(frequencies, power_filt2, color = 'red')
plt.axvline(power_med8, color = 'red')
plt.title('Raw and Filtered Power Spectrum with Meadian Line')
plt.ylabel('Power (a.u.)')
plt.xlabel('Frequency (Hz)')

    #Fatigue 3 End

power, frequencies = l3f.get_power(arrayend3, 400)
b2, a2 = sp.signal.butter(4, 0.08, btype='lowpass')
power_filt3 = sp.signal.filtfilt(b2, a2, power)
power_med9 = np.median(power_filt3)

plt.figure()
plt.plot(frequencies, power)
plt.plot(frequencies, power_filt3, color = 'red')
plt.axvline(power_med9, color = 'red')
plt.title('Raw and Filtered Power Spectrum with Meadian Line')
plt.ylabel('Power (a.u.)')
plt.xlabel('Frequency (Hz)')
    
    #Question 11
    
    #Power Spectrum Median

values1 = [power_med1, power_med2, power_med3]
values2 = [power_med4, power_med5, power_med6]
values3 = [power_med7, power_med8, power_med9]
time_of_measurements = [0.1, 0.5, 0.9]

plt.figure()
plt.plot(time_of_measurements, values1, color = 'black')
plt.plot(time_of_measurements, values2, color = 'black')
plt.plot(time_of_measurements, values3, color = 'black')
plt.ylabel('Median Frequency (Hz)')
plt.xlabel('Time of Measurement (%)')
plt.title('Question 11 Power Spectrum Median of 3 Fatigue Trials')
plt.plot(0.1, power_med1, marker = '*', markersize=12, color = 'red', label = 'Start of Trial')
plt.plot(0.1, power_med4, marker = '*', markersize=12, color = 'red')
plt.plot(0.1, power_med7, marker = '*', markersize=12, color = 'red')
plt.plot(0.5, power_med2, marker = '*', markersize=12, color = 'blue', label = 'Middle of Trial')
plt.plot(0.5, power_med5, marker = '*', markersize=12, color = 'blue')
plt.plot(0.5, power_med8, marker = '*', markersize=12, color = 'blue')
plt.plot(0.9, power_med3, marker = '*', markersize=12, color = 'darkorange', label = 'End of Trial')
plt.plot(0.9, power_med6, marker = '*', markersize=12, color = 'darkorange')
plt.plot(0.9, power_med9, marker = '*', markersize=12, color = 'darkorange')
plt.legend()

