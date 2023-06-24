# Documentation for Elliptic Curve Point Addition

This Python code provides functionality for adding points on an elliptic curve over a finite field. 

Here is the algorithm for calculating the addition of two points $P$ and $Q$ on the elliptic curve $y^2 = x^3 + ax + b$  in a given prime field $F$:

1. If $P = 0$, then $P + Q = Q$
2. Otherwise, if $Q = 0$, then $P + Q = P$
3. Otherwise, write $P = (x_1, y_1)$ and $Q = (x_2,y_2)$
4. If $x_1 = x_2$ and $y_1 = - y_2$, then $P + Q = 0$.
5. Otherwise:
	- if $P \neq Q$: $\lambda = \frac{y_2 - y_1}{x_2 - x_1} \mod F$
	- if $P = Q$: $\lambda = \frac{3x_1^2 + a}{2*y_1} \mod F$
6. Calculation of $x_3,y_3$ is done as follows:
	-  $x_3 = \lambda^2 - x_1 - x_2 \mod F$
	-  $y_3 = \lambda*( x_1 - x_3) - y_1 \mod F$
7. $P + Q = (x_3,y_3)$

**Note** 
- $0$ here denotes "the point at infinity" (often represented as $(0,0)$ ), typically used as the identity element for the group operation (i.e., point addition). This is effectively the "zero" of the elliptic curve.

- Also note that the division in a prime field $F$ is done as follows. Let's say we want to do a division in the prime field $F$ for the following fraction $x/y \mod F$, then it will be calculated as $x \cdot y^{F-2} \mod F$ following [Fermat's little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem) where `pow` function returns the value of $x$ to the power of $y$ in the prime field $F$. 

## Functions

### `is_on_curve(x, y, a, b, F)`

This function checks whether a point `(x, y)` lies on the elliptic curve defined by the equation $y^2 = x^3 + ax + b$ over the finite field `F`.

#### Parameters

- `x`: The x-coordinate of the point.
- `y`: The y-coordinate of the point.
- `a`, `b`: The coefficients of the elliptic curve equation.
- `F`: The order of the finite field.

#### Returns

- `True` if the point `(x, y)` lies on the elliptic curve, and `False` otherwise.

### `add_points(points, a, b, F)`

This function adds a list of points on an elliptic curve over a finite field.

#### Parameters

- `points`: A list of tuples, each tuple representing a point on the curve.
- `a`, `b`: The coefficients of the elliptic curve equation.
- `F`: The order of the finite field.


#### Returns

- A tuple representing the sum of all points in the list. If any point in the list does not lie on the curve, the function returns `None`.

### Example Usage

```python
# Define the points
points = [(493, 5564), (493, 5564), (1539, 4742), (4403, 5202)]

# Define the elliptic curve parameters and the finite field order
a = 497
b = 1768
F = 9739

# Check if a point is on the curve
print(is_on_curve(x=493, y=5564, a=a, b=b, F=F))

# Add points on the curve
print(add_points(points=points, a=a, b=b, F=F))
```
