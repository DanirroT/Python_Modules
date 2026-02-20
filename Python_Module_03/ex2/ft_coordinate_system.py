#!/usr/bin/env python3

import sys

def ft_calc_distance(statrt: tuple[float, float, float], end: tuple[float, float, float]) -> float:
    """Calculate the distance between two points in 3D space."""
    if statrt is None or end is None:
        return None
    x1, y1, z1 = statrt
    x2, y2, z2 = end
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5


def ft_parse_coordinates(coord_str: str) -> tuple[int, int, int] | None:
    """Parse a string of the format 'x,y,z' into a tuple of integers."""
    print("Parsed position:", coord_str)
    try:
        split_coords = coord_str.split(",")
        x_str, y_str, z_str = split_coords
        x = int(x_str.strip())
        y = int(y_str.strip())
        z = int(z_str.strip())
        return (x, y, z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)")
        return None



def ft_coordinate_system(scores_str: list[str]) -> None:
    print("=== Game Coordinate System ===")
    origin = (0, 0, 0)
    print()
    point_a = (10, 20, 5)
    print(f"Position created: {point_a}")
    print(f"Distance between {origin} and {point_a}: {ft_calc_distance(origin, point_a):.2f}")
    print()
    point_b_str = "3,4,0"
    print(f"Parsing coordinates: \"{point_b_str}\"")
    point_b = ft_parse_coordinates(point_b_str)
    print(f"Distance between {origin} and {point_b}: {ft_calc_distance(origin, point_b):.2f}")
    print()
    point_c_str = "abc,def,ghi"
    print(f"Parsing coordinates: \"{point_c_str}\"")
    point_c = ft_parse_coordinates(point_c_str)
    print(f"Distance between {origin} and {point_c}: {ft_calc_distance(origin, point_c):.2f}")
    print()
    print("Unpacking demonstration:")
    print(f"Player at x={point_b[0]}, y={point_b[1]}, z={point_b[2]}")
    x, y, z = point_b
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

if __name__ == "__main__":
    ft_coordinate_system(sys.argv[1:])
