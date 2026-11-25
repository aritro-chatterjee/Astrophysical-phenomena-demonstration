# Astrophysical-phenomena-demonstration
This repository contains the Python framework for some basic astrophysical phenomena, namely variation of shadow length of a vertical object with the latitudes, the solar path tracing on the celestial sphere, and a solar spectra fitting with respect to the blackbody radiation curve.

1. **Variation Of Shadow Length Of Pole For Varying Latitudes**

The length of the shadow L of a pole of height H at local solar noon depends on the solar altitude angle α, which varies with the latitude ϕ and the solar declination δ. The solar declination varies cyclically throughout the year and is approximated by **δ = 23.44◦ × sin(2π × day/365)**, where day counts days from the start of the year.
At solar noon, the solar altitude angle is **α = 90◦ − (ϕ − δ)**, so the shadow length is given by **L = H × tan(ϕ − δ)**.
Plotting L with progression of days shows how the pole’s shadow length changes seasonally for different latitudes, including for home location ϕ.

• The curve with latitude 30◦ is close to the equator and thus shadow lengths are shorter and vary less over the year. The curve with latitude 60◦ is close to the poles and hence sun’s altitude changes drastically with seasons and shadows are longer.

• All the curves have two minima, at the summer solstice (highest elevation angle of the sun) due to which shadow length is shortest. The maxima for the curves is at the winter solstice where the elevation angle of the sun is the lowest, thus resulting in longest shadow length.

• An interesting thing to note is that for latitudes more than 66.5°, the shadow length tends to ±∞ as the altitude α becomes 0°, causing ϕ − δ to become 90°, thus leading to divergence of the shadow length. The curve goes to both +∞ and −∞ because the altitude is in the tan function, so the graphical shape is similar to that of the tan curve.

2. **Solar Path At Given Latitude On The Celestial Sphere**

The apparent path of the Sun across the sky at a given latitude ϕ and solar declination δ can be described using the hour angle H. The hour angle at sunrise or sunset H0 is given by **H0 = arccos(−tan ϕ tan δ)**. The solar elevation angle α and azimuth A at any hour angle H are:
                                                **α = arcsin(sin ϕ sin δ + cos ϕ cos δ cosH)
                                                  A = arctan 2(−sinH, tan δ cos ϕ − sin ϕ cosH)**
The azimuth A is measured from the north point eastward (0◦ to 360◦). Plotting α against A for different declinations (equinox and solstice) visualizes the Sun’s path as seen from the observer’s location.

• We observe that for summer solstice **(δ=23.44◦)**, the sun is at the highest point in the sky (maximum altitude) for the longest duration, due to which the curve is static once the maximum altitude is achieved, after which the altitude again decreases as the sun is about to set.

• For the vernal equinox **(δ=0◦)**, the curve is symmetric, showing that the length of day and night are the same.

• For the winter solstice **(δ=−23.44◦)**, the maximum altitude achieved is minimum compared to the other two curves, which means that the sun is at the lowest point in the sky and for the least duration.

3. **Solar Spectra and Blackbody Radiation**

The Sun’s emitted spectrum approximates a blackbody spectrum. Given experimental solar spectral data (wavelength vs. flux), the Sun’s effective temperature T can be estimated using Wien’s displacement law, **λ_max x T = 2.89 × 10−3 m · K**, where λmax is the wavelength at maximum flux. The Planck radiation law describes the spectral radiance of a blackbody radiator:
                                                **Bλ(λ, T) = (2hc^2/λ^5) x 1/(exp(hc/λkT) − 1)**
where h is Planck’s constant, c the speed of light, k the Boltzmann constant, λ the wavelength, and T the temperature.

The solar spectrum shows absorption lines caused by elements in the solar atmosphere absorbing light at specific wavelengths. Some prominent absorption lines and their identifying elements are:
• Fe (Iron) at 3581.21 ˚A
• Ca (Calcium) at 4307.74 ˚A
• Ni (Nickel) at 2994.44 ˚A


• The blackbody spectra is plotted corresponding to the solar spectral data provided. Using Wien’s displacement law, the wavelength corresponding to the maximum solar flux is found to be 4510 ˚A.

• Assuming the sun to be a blackbody, it’s surface temperature is calculated using the Planck’s radiation law, which is found to be 6407.982 K, which is a slight deviation from the actual value, which is 5800 K.

• The absorption lines appear as dips in the solar spectrum and are marked on the plot for spectral analysis.
