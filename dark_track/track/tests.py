from django.test import TestCase

# Create your tests here.
def test_geo():
    from django.contrib.gis.gdal import DataSource
    ds = DataSource('task/Pole.shp')

    print(ds)


if __name__ == '__main__':
    test_geo()
