### Variation Of Shadow Length Of Pole For Varying Latitudes

import numpy as np
import matplotlib.pyplot as plt

l1,l2,l3=42,56,60 #given latitudes
l4=eval(input("latitude of home town (Delhi in my case):"))

H=1 #height of pole
n=2 #step size for no. of days
L=[l1,l2,l3,l4]

days=np.arange(0,551,n)
def delta(n):
     return 23.44*(np.sin((2*np.pi*(days))/(365)))

plt.figure(figsize=(10, 6))
for i in L:
     length=H*(np.tan(np.radians(np.abs(delta(n)-i))))
     plt.plot(days,length,label=f'latitude = {i}')
plt.title('Variation of shadow length of 1m pole for changing latitudes')
plt.xlabel('progression of days')
plt.ylabel('length of shadow in meters')
plt.grid()
plt.legend()
plt.show()



### Solar Path At Given Latitude On The Celestial Sphere

import numpy as np
import matplotlib.pyplot as plt

latitude = eval(input("enter latitude:"))
declinations = [-23.44, 0, 23.44]  # in degrees
phi = np.deg2rad(latitude)

plt.figure(figsize=(10,6))

for dec in declinations:
     delta = np.deg2rad(dec)
     H0=np.arccos(-np.tan(phi) * np.tan(delta))
     H = np.linspace(-H0, H0, 4000)

     a = np.arcsin(np.sin(phi)*np.sin(delta) + np.cos(phi)*np.cos(delta)*np.cos(H))
     A = np.arctan2(-np.sin(H), np.tan(delta)*np.cos(phi) - np.sin(phi)*np.cos(H))

     plt.plot((np.degrees(A) + 360) % 360, np.degrees(a), label=f"Declination = {dec}$\degree$")

plt.xlabel("Solar azimuth angle ($\degree$)")
plt.ylabel("Solar elevation angle ($\degree$)")
plt.ylim(0, 90)
plt.title(f"Sun path for different declinations at latitude = {latitude}$\degree$")
plt.grid()
plt.legend()
plt.show()



### Solar Spectra and Blackbody Radiation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#using pandas library to import the data file
df = pd.read_excel('C:/Users/aritr/OneDrive/Desktop/converted_file.xlsx')
wav = df.iloc[::, 0].reset_index(drop=True)   
flux = df.iloc[::, 1].reset_index(drop=True)   

# finding lambda for max flux
fluxmax = flux.idxmax()                       
lambdamax = wav[fluxmax]                     

# wien's displacement law
T = 2.89*10**(-3) / (lambdamax * 10**(-10))

print(f"λ_max = {lambdamax} Angstrom")
print(f"T = {T:.3f} K")


wav1 = df.iloc[:,0].to_numpy()*10**(-10)   # Angstrom to meters
flux1 = df.iloc[:,1].to_numpy()

# We implement Planck's radiation law
h= 6.626*10**(-34)
c=3*10**8
k=1.381*10**(-23)
bbr = (2*h*c**2/wav1**5)/(np.exp(h*c/(wav1*k*T))-1)

# Scaling to match solar spectral data peak
bbr = bbr* (flux1.max()/bbr.max())


#plotting
plt.figure(figsize=(10, 6))
plt.plot(wav, flux,label='Solar spectra')
plt.plot(wav1*10**10, bbr, 'r--', label="Blackbody spectra")
plt.xlabel('Wavelength of solar radiation ($\\AA$)')
plt.ylabel('Solar spectral flux ($Watt / m^2 \\AA$)')
plt.title('Solar spectra vs fitted blackbody spectra')
plt.grid()
plt.legend()
plt.show()


#absorption spectral lines plot
plt.figure(figsize=(10, 6))
plt.plot(wav, flux,label='Solar spectra')
plt.axvline(x=3581.21, color='red', linestyle='-', label='Fe (N) spectral line')
plt.axvline(x=3970.47, color='black', linestyle='-', label='Ca$^+$(H) spectral line')
plt.axvline(x=2994.44, color='orange', linestyle='-', label='Ni (t) spectral line')
plt.xlim(2800,4200)
plt.xlabel('Wavelength of solar radiation ($\\AA$)')
plt.ylabel('Solar spectral flux ($Watt / m^2 \\AA$)')
plt.title('Spectral lines on the solar spectra')
plt.grid()
plt.legend()
plt.show()
