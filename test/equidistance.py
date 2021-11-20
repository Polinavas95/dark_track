import matplotlib.pyplot as plt
import numpy as np
import shapely.geometry as geom
from shapely.ops import transform

from pprint import pprint

from pyproj import Transformer, Proj

ecef = Proj(proj='geocent', ellps='WGS84', datum='WGS84')
lla = Proj(proj='latlong', ellps='WGS84', datum='WGS84')

tocartesian = Transformer.from_proj(lla, ecef, always_xy=True).transform

import fiona

shape = fiona.open(r"D:\MyCodes\Projects\agrohack21\task\Pole.shp")
# first feature of the shapefile
first = next(iter(shape))

# Create a Polygon from the nx2 array in `afpts`
afpoly = geom.shape(first["geometry"])
#A = afpoly
A = transform(tocartesian, afpoly)
B = A.boundary.parallel_offset(distance=2.8, side="right", join_style=1)
C = B.parallel_offset(distance=2.8, side="left", join_style=1)

As = np.array(A.exterior)
Bs = np.array(B)
Cs = np.array(C)
# Plot points
plt.plot(*As.T, color='black')
plt.plot(*Bs.T, color='red')
plt.plot(*Cs.T, color='green')

# plt.plot(*noffafpolypts.T, color='green')
plt.axis('equal')
plt.show()
