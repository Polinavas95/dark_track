import matplotlib.pyplot as plt
import shapely.geometry as geom
from math import tan, radians
from shapely.ops import transform
from pyproj import Transformer, Proj
import fiona

agg_width = 8 * 0.7
turn_radius = 5

def equation(k, b):
    def _(x):
        return k * x + b
    return _


def distance(point, apoint):
    return ((point.x - apoint.x) ** 2 + (point.y - apoint.y) ** 2) ** 0.5


def process_contour(processing_area, maxdepth):
    contour_route = []
    processed_boundary = []
    for i in range(maxdepth):
        route = processing_area.boundary.parallel_offset(distance=(agg_width) * (i + 0.5), side="right", join_style=1)
        boundary = processing_area.boundary.parallel_offset(distance=(agg_width) * (i + 1), side="right", join_style=1)
        contour_route.append(route)
        processed_boundary.append(boundary)
    return contour_route, processed_boundary


def sectorize(contour, pattern_line, maxsteps=100, step_width=agg_width):
    intersections = []
    lines = {"left": [], "right": []}
    norotating_area = geom.Polygon(contour.parallel_offset(turn_radius + agg_width / 2, side="left"))
    for side in "left", "right":
        for i in range(0, maxsteps):
            if i == 0:
                if side == "right":
                    new_line = pattern_line
                else:
                    continue
            new_line = pattern_line.parallel_offset(i * step_width, side)
            _ = new_line.intersection(norotating_area.boundary)
            if isinstance(_, geom.MultiPoint):
                intersection = list(map(lambda p: (p.x, p.y), [*_]))
                if len(intersection) > 2:
                    lines[side] += [*new_line.intersection(norotating_area)]
                else:
                    lines[side].append(new_line.intersection(norotating_area))
            elif isinstance(_, geom.Point):
                intersection = [(_.x, _.y)]
                lines[side].append(new_line.intersection(norotating_area))
            else:
                break

            intersections += intersection
    intersection_lines = [*lines["left"], *lines["right"]]
    return intersections, intersection_lines, norotating_area

# x0 = 3411342.2363809124
# y0 = 1736246.1740086577

# b =  1736246 - 0.017 * 3411342
# y(x) = 0.017 * x + 3381035
#

def intersect_sectors2contour(contour, x0, y0, minx, maxx, minangle=1, maxangle=180, stepangle=5):
    intersections = {}
    intersections_lines = {}
    norotate_area = {}
    for alpha in range(minangle, maxangle, stepangle):
        k = tan(radians(alpha))
        b = y0 - k * x0
        y = equation(k, b)
        p0, p1 = (minx, y(minx)), (maxx, y(maxx))
        uncropped_line = geom.LineString([p0, p1])
        intersections[alpha], intersections_lines[alpha], norotate_area[alpha] = \
            sectorize(contour, uncropped_line)
    return intersections, intersections_lines, norotate_area


def get_best_alpha(intersections):
    minimal = None
    best_alpha = None
    for alpha, points in intersections.items():
        if minimal is None or len(points) < minimal:
            minimal = len(points)
            best_alpha = alpha
    return best_alpha, minimal


# # Plot points
# plt.plot(*processing_area.exterior.xy, color='black')
# plt.plot(*contour_route[2].xy, color='red')
# plt.plot(*rectangular.exterior.xy, color='green', linestyle="dashed")
#
# for line in intersections_lines[86]:
#     try:
#         plt.plot(*line.xy, color='gray', alpha=0.5)
#     except:
#         print("nope")
# plt.scatter(*zip(*intersections[86]), color='blue', s=1)
# plt.plot(*center, color='purple', marker='+')
#
# plt.axis('equal')
# plt.show()


if __name__ == '__main__':
    ecef = Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    lla = Proj(proj='latlong', ellps='WGS84', datum='WGS84')
    tocartesian = Transformer.from_proj(lla, ecef, always_xy=True).transform

    shape = fiona.open(r"D:\MyCodes\Projects\agrohack21\task\Pole.shp")
    first = next(iter(shape))

    input_field = geom.shape(first["geometry"])
    processing_area = transform(tocartesian, input_field)
    rectangular = processing_area.minimum_rotated_rectangle
    center = (processing_area.centroid.x, processing_area.centroid.y)
    minx, maxx = rectangular.bounds[0], rectangular.bounds[2]

    contour_route, processed_boundary = process_contour(processing_area, 3)
    intersections, intersections_lines, norotate_area = \
        intersect_sectors2contour(processed_boundary[0], center[0], center[1], minx, maxx)

    plt.plot(*processing_area.exterior.xy, color='black')
    plt.plot(*contour_route[0].xy, color='red')
    plt.plot(*processed_boundary[0].xy, color='green', alpha=0.2)
    plt.plot(*center, marker="+")

    for line in intersections_lines[86]:
        try:
            plt.plot(*line.xy, color='gray', alpha=0.5)
        except:
            print("nope")

    plt.axis('equal')
    plt.show()
    a = intersections_lines[1]
    print('a')
