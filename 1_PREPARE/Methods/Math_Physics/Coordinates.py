import sys
import math
import numpy as np
from typing import Tuple, Union

# Dynamically append the qrays.py module from the Math4Wisdom repository to the system path for importing
sys.path.append('../../9_OTHER/repos/Synergetics/m4w')
from qrays import Vector, Qvector

class VectorAdapter:
    """
    A sophisticated class designed to seamlessly adapt between Cartesian (XYZ), Internal Volume Metric (IVM or quadray),
    and concentric spherical coordinate systems leveraging the Vector and Qvector classes. This adapter facilitates
    the conversion and manipulation of vectors across different geometric representations, enhancing analytical capabilities
    in mathematical and physical computations.
    """

    def __init__(self, coords: Union[Tuple[float, float, float], Tuple[float, float, float, float]], coord_type: str = 'xyz'):
        """
        Constructs a VectorAdapter instance initialized with coordinates in either Cartesian, IVM, or concentric spherical formats.

        Args:
            coords (Union[Tuple[float, float, float], Tuple[float, float, float, float]]): The coordinates to be adapted.
            coord_type (str, optional): The type of coordinate system ('xyz' for Cartesian, 'ivm' for quadray, or 'concentric' for spherical). Defaults to 'xyz'.

        Raises:
            ValueError: If an unsupported coordinate type is specified.
        """
        self.coord_type = coord_type.lower()
        self.vector: Union[Vector, None] = None
        self.qvector: Union[Qvector, None] = None
        self.concentric_coords: Union[Tuple[float, float, float], None] = None

        if self.coord_type == 'xyz':
            self.vector = Vector(coords)
            self.qvector = self.vector.quadray()
        elif self.coord_type == 'ivm':
            self.qvector = Qvector(coords)
            self.vector = self.qvector.xyz()
        elif self.coord_type == 'concentric':
            self.concentric_coords = coords
            self._update_vector_from_concentric()
        else:
            raise ValueError(f"Unsupported coordinate type specified: {coord_type}")

    def _update_vector_from_concentric(self) -> None:
        """
        Updates the Cartesian vector representation from concentric spherical coordinates.
        """
        r, theta, phi = self.concentric_coords
        x = r * math.sin(theta) * math.cos(phi)
        y = r * math.sin(theta) * math.sin(phi)
        z = r * math.cos(theta)
        self.vector = Vector((x, y, z))

    def to_xyz(self) -> Vector:
        """
        Efficiently converts and returns the stored coordinates in Cartesian (XYZ) format.

        Returns:
            Vector: The coordinates in Cartesian format.
        """
        if self.coord_type != 'xyz':
            if self.coord_type == 'concentric':
                self._update_vector_from_concentric()
            else:
                self.vector = self.qvector.xyz()
            self.coord_type = 'xyz'
        return self.vector

    def to_ivm(self) -> Qvector:
        """
        Efficiently converts and returns the stored coordinates in IVM (quadray) format.

        Returns:
            Qvector: The coordinates in IVM format.
        """
        if self.coord_type != 'ivm':
            self.qvector = self.vector.quadray()
            self.coord_type = 'ivm'
        return self.qvector

    def to_concentric(self) -> Tuple[float, float, float]:
        """
        Efficiently converts and returns the stored coordinates in concentric spherical format.

        Returns:
            Tuple[float, float, float]: The coordinates in concentric spherical format (r, theta, phi).
        """
        if self.coord_type != 'concentric':
            x, y, z = self.vector.xyz()
            r = math.sqrt(x**2 + y**2 + z**2)
            theta = math.acos(z / r) if r != 0 else 0
            phi = math.atan2(y, x)
            self.concentric_coords = (r, theta, phi)
            self.coord_type = 'concentric'
        return self.concentric_coords

    def __repr__(self) -> str:
        """
        Generates a sophisticated representation of the VectorAdapter instance, showcasing the current coordinate system and values.

        Returns:
            str: A string representation of the vector in its current coordinate system.
        """
        if self.coord_type == 'xyz':
            x, y, z = self.vector.xyz()
            return f"XYZ Vector(x={x:.4f}, y={y:.4f}, z={z:.4f})"
        elif self.coord_type == 'ivm':
            a, b, c, d = self.qvector.coords
            return f"IVM Vector(a={a:.4f}, b={b:.4f}, c={c:.4f}, d={d:.4f})"
        else:
            r, theta, phi = self.concentric_coords
            return f"Concentric Vector(r={r:.4f}, θ={math.degrees(theta):.2f}°, φ={math.degrees(phi):.2f}°)"

    def __add__(self, other: 'VectorAdapter') -> 'VectorAdapter':
        """
        Implements vector addition, returning a new VectorAdapter instance in Cartesian format.

        Args:
            other (VectorAdapter): The vector to add.

        Returns:
            VectorAdapter: A new VectorAdapter instance representing the sum of the vectors.
        """
        new_vector = self.vector + other.to_xyz()
        return VectorAdapter(new_vector.xyz(), 'xyz')

    def __sub__(self, other: 'VectorAdapter') -> 'VectorAdapter':
        """
        Implements vector subtraction, returning a new VectorAdapter instance in Cartesian format.

        Args:
            other (VectorAdapter): The vector to subtract.

        Returns:
            VectorAdapter: A new VectorAdapter instance representing the difference of the vectors.
        """
        new_vector = self.vector - other.to_xyz()
        return VectorAdapter(new_vector.xyz(), 'xyz')

    def __mul__(self, scalar: float) -> 'VectorAdapter':
        """
        Implements scalar multiplication, returning a new VectorAdapter instance scaled in Cartesian format.

        Args:
            scalar (float): The scalar value to multiply the vector by.

        Returns:
            VectorAdapter: A new VectorAdapter instance representing the scaled vector.
        """
        new_vector = self.vector * scalar
        return VectorAdapter(new_vector.xyz(), 'xyz')

    def __truediv__(self, scalar: float) -> 'VectorAdapter':
        """
        Implements scalar division, returning a new VectorAdapter instance scaled down in Cartesian format.

        Args:
            scalar (float): The scalar value to divide the vector by.

        Returns:
            VectorAdapter: A new VectorAdapter instance representing the scaled-down vector.

        Raises:
            ValueError: If the scalar is zero.
        """
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        new_vector = self.vector / scalar
        return VectorAdapter(new_vector.xyz(), 'xyz')

    def dot(self, other: 'VectorAdapter') -> float:
        """
        Calculates and returns the dot product with another vector, enhancing vector analysis capabilities.

        Args:
            other (VectorAdapter): The vector to calculate the dot product with.

        Returns:
            float: The dot product of the two vectors.
        """
        return self.vector.dot(other.to_xyz())

    def cross(self, other: 'VectorAdapter') -> 'VectorAdapter':
        """
        Calculates and returns the cross product with another vector, facilitating vectorial computations in 3D space.

        Args:
            other (VectorAdapter): The vector to calculate the cross product with.

        Returns:
            VectorAdapter: A new VectorAdapter instance representing the cross product.
        """
        new_vector = self.vector.cross(other.to_xyz())
        return VectorAdapter(new_vector.xyz(), 'xyz')

    def length(self) -> float:
        """
        Returns the magnitude of the vector, providing insights into vector length in the current coordinate system.

        Returns:
            float: The magnitude of the vector.
        """
        return self.vector.length()

    def angle_with(self, other: 'VectorAdapter') -> float:
        """
        Calculates and returns the angle with another vector, aiding in the analysis of vector orientations.

        Args:
            other (VectorAdapter): The vector to calculate the angle with.

        Returns:
            float: The angle between the two vectors in radians.
        """
        return self.vector.angle(other.to_xyz())

    def spherical(self) -> Tuple[float, float, float]:
        """
        Returns the spherical coordinates of the vector, offering an alternative geometric perspective.

        Returns:
            Tuple[float, float, float]: The spherical coordinates (r, theta, phi) in radians.
        """
        return self.vector.spherical()

    def quadray(self) -> Tuple[float, float, float, float]:
        """
        Returns the quadray (IVM) coordinates of the vector, enriching the geometric analysis toolkit.

        Returns:
            Tuple[float, float, float, float]: The quadray coordinates (a, b, c, d).
        """
        return self.qvector.coords

    def normalize(self) -> 'VectorAdapter':
        """
        Returns a new VectorAdapter instance with the normalized vector.

        Returns:
            VectorAdapter: A new VectorAdapter instance representing the normalized vector.
        """
        normalized = self.vector.normalize()
        return VectorAdapter(normalized.xyz(), 'xyz')

    def rotate(self, axis: 'VectorAdapter', angle: float) -> 'VectorAdapter':
        """
        Rotates the vector around a specified axis by a given angle.

        Args:
            axis (VectorAdapter): The axis of rotation.
            angle (float): The angle of rotation in radians.

        Returns:
            VectorAdapter: A new VectorAdapter instance representing the rotated vector.
        """
        axis_vector = axis.to_xyz()
        rotated = self.vector.rotate(axis_vector, angle)
        return VectorAdapter(rotated.xyz(), 'xyz')

    def project(self, other: 'VectorAdapter') -> 'VectorAdapter':
        """
        Projects this vector onto another vector.

        Args:
            other (VectorAdapter): The vector to project onto.

        Returns:
            VectorAdapter: A new VectorAdapter instance representing the projected vector.
        """
        projected = self.vector.project(other.to_xyz())
        return VectorAdapter(projected.xyz(), 'xyz')

    def __format__(self, format_spec: str) -> str:
        """
        Enables custom formatting for printing, showcasing the vector's representation according to the specified format.

        Args:
            format_spec (str): The format specification string.

        Returns:
            str: The formatted string representation of the vector.
        """
        if self.coord_type == 'xyz':
            return f"{self.vector.__str__():{format_spec}}"
        elif self.coord_type == 'ivm':
            return f"{self.qvector.__str__():{format_spec}}"
        else:
            return f"{self.concentric_coords.__str__():{format_spec}}"

if __name__ == "__main__":
    headers = ["Operation", "Initial Vector", "Converted Vector"]
    test_vectors = [
        {"description": "XYZ to IVM", "vector": VectorAdapter((1.0, 2.0, 3.0), 'xyz'), "conversion_method": "to_ivm"},
        {"description": "IVM to XYZ", "vector": VectorAdapter((1, 1, 1, 1), 'ivm'), "conversion_method": "to_xyz"},
        {"description": "Vector Addition (XYZ) and Convert to IVM", "vector": VectorAdapter((1.0, 0.0, 0.0), 'xyz') + VectorAdapter((0.0, 1.0, 0.0), 'xyz'), "conversion_method": "to_ivm"},
        {"description": "Concentric to XYZ", "vector": VectorAdapter((1.0, math.pi/4, math.pi/3), 'concentric'), "conversion_method": "to_xyz"},
        {"description": "Vector Normalization", "vector": VectorAdapter((3.0, 4.0, 0.0), 'xyz').normalize(), "conversion_method": "to_xyz"},
        {"description": "Vector Rotation", "vector": VectorAdapter((1.0, 0.0, 0.0), 'xyz').rotate(VectorAdapter((0.0, 0.0, 1.0), 'xyz'), math.pi/2), "conversion_method": "to_xyz"},
    ]

    # Formatting table header
    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "+" + "-" * (len(header_line) - 2) + "+"
    print(header_line)
    print(separator_line)

    # Processing and displaying each test vector
    for test_vector in test_vectors:
        initial_vector = test_vector["vector"]
        conversion_method = test_vector["conversion_method"]
        converted_vector = getattr(initial_vector, conversion_method)()
        print(f"| {test_vector['description']:40} | {initial_vector:30} | {converted_vector} |")

    # Calculating and displaying dot product and angle
    vec_ivm = VectorAdapter((1, 1, 1, 1), 'ivm')
    vec2_xyz = VectorAdapter((0.0, 1.0, 0.0), 'xyz')
    dot_product = vec_ivm.dot(vec2_xyz)
    angle = vec_ivm.angle_with(vec2_xyz)
    angle_display = f"{math.degrees(angle):.2f} degrees" if not math.isnan(angle) else "NaN"
    print(f"| {'Dot Product and Angle':40} | {'vec_ivm & vec2_xyz':30} | {dot_product:.4f}, {angle_display} |")

    # Additional operations
    cross_product = vec_ivm.cross(vec2_xyz)
    projection = vec_ivm.project(vec2_xyz)
    print(f"| {'Cross Product':40} | {'vec_ivm x vec2_xyz':30} | {cross_product} |")
    print(f"| {'Vector Projection':40} | {'vec_ivm onto vec2_xyz':30} | {projection} |")

