def is_on_curve(x, y, a, b, F):
    """
    Check whether a point lies on a given elliptic curve in a finite field.

    Parameters:
    x (int): The x-coordinate of the point.
    y (int): The y-coordinate of the point.
    a, b (int): The coefficients of the elliptic curve equation.
    F (int): The order of the finite field.

    Returns:
    bool: True if the point lies on the curve, False otherwise.
    """
    return (pow(y, 2, F) - (pow(x, 3, F) + a*x % F + b)) % F == 0


def add_points(points, a, b, F):
    """
    Add a list of points on an elliptic curve over a finite field.

    Parameters:
    points (list): A list of tuples, each tuple representing a point on the curve.
    a, b (int): The coefficients of the elliptic curve equation.
    F (int): The order of the finite field.

    Returns:
    tuple: A tuple representing the sum of all points in the list. If any point in the list 
    does not lie on the curve, the function returns None.
    """
    # Start with the point at infinity
    result = (None, None)

    for point in points:
        x, y = point[0] % F, point[1] % F

        if not is_on_curve(x, y, a, b, F):
            return None

        # handle the special cases when one of the point is "at infinity"
        if result == (None, None):
            result = point
            continue

        x_1, y_1 = result
        x_2, y_2 = point

        # if P and Q are inverses, return point at infinity
        if x_1 == x_2 and y_1 == (-y_2 % F):
            result = (None, None)
            continue

        # calculating the slope
        if result != point:
            s = (y_2 - y_1) * pow(x_2 - x_1, F - 2, F)
        else:
            s = (3 * pow(x_1, 2, F) + a) * pow(2 * y_1, F - 2, F)

        # calculating the third point
        summed_x = (pow(s, 2, F) - x_1 - x_2) % F
        summed_y = (s * (x_1 - summed_x) % F - y_1) % F

        result = (summed_x, summed_y)

    return result


def main():
    print("Enter the coefficients of the elliptic curve equation y^2 = x^3 + ax + b over a prime finite field F.")
    a = int(input("For the Enter the coefficient a: "))
    b = int(input("Enter the coefficient b: "))
    F = int(input("Enter the prime field order F: "))

    points = []
    while True:
        x = input("Enter the x-coordinate of a point (or 'q' to quit): ")
        if x.lower() == 'q':
            break
        y = int(input("Enter the y-coordinate of the same point: "))
        points.append((int(x), y))

    result = add_points(points, a, b, F)
    if result is None:
        print("One or more points are not on the elliptic curve.")
    else:
        print("The sum of the points is:", result)


if __name__ == "__main__":
    main()
