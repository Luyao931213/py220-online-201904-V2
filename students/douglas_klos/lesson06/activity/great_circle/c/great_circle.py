#!/usr/bin/env python3
import great_circle


lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826

if __name__ == "__main__":

    for i in range(10000000):
        great_circle.great_circle(lon1, lat1, lon2, lat2)
