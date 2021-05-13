import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft

#导入数据
file_path="F:\experimentData1\jupyter_file\maibojiance\脉搏波数据文件\采样者2\静坐采样数据.txt"
f=open(file_path)
data_1=pd.read_csv(f, sep='\s+')  #空格不一致读取方式

#数据格式转换
data_ired_list=[]
for data_ired in data_1["ired"]:
    data_ired_list.append(data_ired)

data_ired_array=np.array(data_ired_list)
#把数据中和前后差异都较大的点筛掉
threshold_delta=500
error_list=[]
if abs(data_ired_array[0]-data_ired_array[1])>threshold_delta:
    error_list.append(0)
if abs(data_ired_array[-1]-data_ired_array[-2])>threshold_delta:
    error_list.append(-1)
for i in range(1,len(data_ired_array)):
    if abs(data_ired_array[i]-data_ired_array[i-1])>threshold_delta and abs(data_ired_array[i]-data_ired_array[i+1])>threshold_delta:
        error_list.append(i)
data_ired_array=np.delete(data_ired_array,error_list)
plt.plot(data_ired_array)

#带通滤波器滤波
import scipy.signal as signal
Fstop1=0.8
Fstop2=2
fs=50
b, a = signal.butter(6, [2.0*Fstop1/fs,2.0*Fstop2/fs], 'bandpass')
filtedData = signal.filtfilt(b,a,data_ired_array)

import math
fft_ired_array=fft(filtedData)
length=len(fft_ired_array)/2
fre=np.arange(length)*25/(length)

low_band=math.ceil(0.8*length/25)
xinlv=abs(fft_ired_array)[low_band:1+math.ceil(length)].argmax()+low_band #高通滤波
xinlv=xinlv*25/(length)*60

