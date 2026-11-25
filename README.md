# Astrophysical-phenomena-demonstration
This repository contains the Python framework for some basic astrophysical phenomena, namely variation of shadow length of a vertical object with the latitudes, the solar path tracing on the celestial sphere, and a solar spectra fitting with respect to the blackbody radiation curve.

The length of the shadow L of a pole of height H at local solar noon depends on the solar altitude angle α, which varies with the latitude ϕ and the solar declination δ. The solar declination varies cyclically throughout the year and is approximated by δ = 23.44◦ × sin(2π × day/365), where day counts days from the start of the year.
At solar noon, the solar altitude angle is α = 90◦ − (ϕ − δ), so the shadow length is given by L = H × tan(ϕ − δ).
Plotting L with progression of days shows how the pole’s shadow length changes seasonally for different latitudes, including for home location ϕ.
• The curve with latitude 30◦ is close to the equator and thus shadow lengths are shorter and vary less over the year. The curve with latitude 60◦ is close to the poles and hence sun’s altitude changes drastically with seasons and shadows are longer.
• All the curves have two minima, at the summer solstice (highest elevation angle of the sun) due to which shadow length is shortest. The maxima for the curves is at the winter solstice where the elevation angle of the sun is the lowest, thus resulting in longest shadow length.
• We observe that for latitudes more than 66.5°, the shadow length tends to ±∞ as the altitude α becomes 0°, causing ϕ − δ to become 90°, thus leading to divergence of the shadow length. The curve goes to both +∞ and −∞ because the altitude is in the tan function, so the graphical shape is similar to that of the tan curve.
