## Part A (bounding box/offset information from the openstreet map)

minlat = 51.4626700

minlon = 5.5899800

maxlat = 51.4751800

maxlon = 5.6255100

import utm

# Southwest
e_sw, n_sw, zone, letter = utm.from_latlon(minlat, minlon)
# Northwest
e_nw, n_nw, _, _ = utm.from_latlon(maxlat, minlon)
# Southeast
e_se, n_se, _, _ = utm.from_latlon(minlat, maxlon)
# Northeast
e_ne, n_ne, _, _ = utm.from_latlon(maxlat, maxlon)

E_min = min(e_sw, e_nw, e_se, e_ne)
E_max = max(e_sw, e_nw, e_se, e_ne)
N_min = min(n_sw, n_nw, n_se, n_ne)
N_max = max(n_sw, n_nw, n_se, n_ne)

x_center = (E_min + E_max) / 2
y_center = (N_min + N_max) / 2

offset_x = x_center
offset_y = y_center

print(f"Offset x: {offset_x:.2f}")
print(f"Offset y: {offset_y:.2f}")

# Example OpenDRIVE coordinates of (approx.) Roselmanserf street
x_odr =  2659.47579395  #2278.46350798 #
y_odr = 112.63688033  #1130.57230420 #

x_offset = offset_x
y_offset = offset_y

# no rotation as "hdg=0"
easting = x_odr + x_offset
northing = y_odr + y_offset

#print(f"easting: {easting}, northing: {northing}")

# UTM zone 31N
zone_number = 31
zone_letter = 'U'  # 'U' covers most of the Netherlands

# Convert to latitude/longitude
lat, lon = utm.to_latlon(easting, northing, zone_number, zone_letter)
print(f"Latitude: {lat}, Longitude: {lon}")

# these lat/long values are near the experimental area however, we need an anchor
# point to correct them or make them more precise