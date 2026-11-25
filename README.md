# Astrophysical-phenomena-demonstration
This repository contains the Python framework for some basic astrophysical phenomena, namely variation of shadow length of a vertical object with the latitudes, the solar path tracing on the celestial sphere, and a solar spectra fitting with respect to the blackbody radiation curve.
Variation Of Shadow Length Of Pole For Varying
Latitudes
Theoretical background
The length of the shadow L of a pole of height H at local solar noon depends
on the solar altitude angle α, which varies with the latitude ϕ and the solar
declination δ. The solar declination varies cyclically throughout the year and is
approximated by
δ = 23.44◦ × sin

2π × day
365

where day counts days from the start of the year.
At solar noon, the solar altitude angle is
α = 90◦ − (ϕ − δ)
so the shadow length is given by
L = H × tan(ϕ − δ)
Plotting L with progression of days shows how the pole’s shadow length changes
seasonally for different latitudes, including for home location ϕ.
