from pyproj import Transformer
import utm

# Reference OpenDRIVE (x, y) and real-world (lat, lon)
x_odr_ref = 2659.47579395
y_odr_ref = 112.63688033
lat_ref = 51.462832
lon_ref = 5.615614

# Convert reference lat/lon to UTM
easting_ref, northing_ref, zone, letter = utm.from_latlon(lat_ref, lon_ref)

# Compute UTM anchor for OpenDRIVE origin
utm_easting_origin = easting_ref - x_odr_ref
utm_northing_origin = northing_ref - y_odr_ref

# Prepare pyproj transformer for UTM zone 31N to WGS84
transformer = Transformer.from_crs("EPSG:32631", "EPSG:4326", always_xy=True)

def odr_to_latlon(x_odr, y_odr):
    utm_easting = x_odr + utm_easting_origin
    utm_northing = y_odr + utm_northing_origin
    lon, lat = transformer.transform(utm_easting, utm_northing)
    return lat, lon

# Example: convert your reference point (should return the original lat/lon)
print("Reference point:", odr_to_latlon(x_odr_ref, y_odr_ref))

# Example: convert another OpenDRIVE (x, y), taken from the opendriven map
x_test = 2792.43349757
y_test = 249.80548940
print("Another point:", odr_to_latlon(x_test, y_test))