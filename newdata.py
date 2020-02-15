import numpy as np
import matplotlib.pyplot as plt
a = np.arange(256)
b = np.fft.fft(np.sin(a))  #傅里叶变换
#a = np.exp(2j * np.pi * np.arange(8) / 8)
#b = np.fft.fft(a)
#c = np.fft.fftfreq(a.shape[-1])  #采样频率
c = np.fft.fftfreq(256)  #采样频率
plt.plot(c,b.real,'-r',c,b.imag)  #real为实部，imag为虚部
