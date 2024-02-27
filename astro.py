from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
import astropy.units as u

obj_coord = SkyCoord(ra=10*u.degree, dec=40*u.degree, frame='icrs')
observer_location = EarthLocation(lat=42*u.deg, lon=72*u.deg, height=0*u.m)
observation_time = Time('2024-02-14 22:00:00')
altaz = obj_coord.transform_to(AltAz(obstime=observation_time, location=observer_location))
print(altaz.alt, altaz.az)
