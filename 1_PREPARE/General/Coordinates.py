import sys
import math
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
    def __init__(self, coords, coord_type='xyz'):
        """
        Constructs a VectorAdapter instance initialized with coordinates in either Cartesian, IVM, or concentric spherical formats.

        Args:
            coords (tuple): The coordinates to be adapted, represented as a tuple.
            coord_type (str, optional): The type of coordinate system ('xyz' for Cartesian, 'ivm' for quadray, or 'concentric' for spherical). Defaults to 'xyz'.
        """
        self.coord_type = coord_type
        if coord_type == 'xyz':
            self.vector = Vector(coords)  # Direct instantiation for Cartesian coordinates
            self.qvector = self.vector.quadray()  # Conversion from Cartesian to quadray coordinates
        elif coord_type == 'ivm':
            self.qvector = Qvector(coords)  # Direct instantiation for quadray coordinates
            self.vector = self.qvector.xyz()  # Conversion from quadray to Cartesian coordinates
        elif coord_type == 'concentric':
            self.concentric_coords = coords  # Direct assignment for concentric spherical coordinates
        else:
            raise ValueError(f"Unsupported coordinate type specified: {coord_type}")

    def to_xyz(self):
        """Efficiently converts and returns the stored coordinates in Cartesian (XYZ) format."""
        if self.coord_type != 'xyz':
            if self.coord_type == 'concentric':
                # Conversion from concentric spherical to Cartesian coordinates
                r, theta, phi = self.concentric_coords
                x = r * math.sin(theta) * math.cos(phi)
                y = r * math.sin(theta) * math.sin(phi)
                z = r * math.cos(theta)
                self.vector = Vector((x, y, z))
            else:
                # Direct conversion from quadray to Cartesian coordinates
                self.vector = self.qvector.xyz()
            self.coord_type = 'xyz'
        return self.vector

    def to_ivm(self):
        """Efficiently converts and returns the stored coordinates in IVM (quadray) format."""
        if self.coord_type != 'ivm':
            # Conversion from Cartesian to quadray coordinates
            self.qvector = self.vector.quadray()
            self.coord_type = 'ivm'
        return self.qvector

    def to_concentric(self):
        """Efficiently converts and returns the stored coordinates in concentric spherical format."""
        if self.coord_type != 'concentric':
            # Conversion from Cartesian to concentric spherical coordinates
            x, y, z = self.vector.xyz()
            r = math.sqrt(x**2 + y**2 + z**2)
            theta = math.acos(z / r)
            phi = math.atan2(y, x)
            self.concentric_coords = (r, theta, phi)
            self.coord_type = 'concentric'
        return self.concentric_coords

    def __repr__(self):
        """Generates a sophisticated representation of the VectorAdapter instance, showcasing the current coordinate system and values."""
        if self.coord_type == 'xyz':
            x, y, z = self.vector.xyz()
            return f"XYZ Vector(x={x:.2f}, y={y:.2f}, z={z:.2f})"
        elif self.coord_type == 'ivm':
            a, b, c, d = self.qvector.coords
            return f"IVM Vector(a={a:.2f}, b={b:.2f}, c={c:.2f}, d={d:.2f})"
        else:
            r, theta, phi = self.concentric_coords
            return f"Concentric Vector(r={r:.2f}, θ={theta:.2f}°, φ={phi:.2f}°)"

    def __add__(self, other):
        """Implements vector addition, returning a new VectorAdapter instance in Cartesian format."""
        new_vector = self.vector + other.to_xyz()
        return VectorAdapter(new_vector.xyz(), 'xyz')

    def __sub__(self, other):
        """Implements vector subtraction, returning a new VectorAdapter instance in Cartesian format."""
        new_vector = self.vector - other.to_xyz()
        return VectorAdapter(new_vector.xyz(), 'xyz')

    def __mul__(self, scalar):
        """Implements scalar multiplication, returning a new VectorAdapter instance scaled in Cartesian format."""
        new_vector = self.vector * scalar
        return VectorAdapter(new_vector.xyz(), 'xyz')

    def __truediv__(self, scalar):
        """Implements scalar division, returning a new VectorAdapter instance scaled down in Cartesian format."""
        new_vector = self.vector / scalar
        return VectorAdapter(new_vector.xyz(), 'xyz')

    def dot(self, other):
        """Calculates and returns the dot product with another vector, enhancing vector analysis capabilities."""
        return self.vector.dot(other.to_xyz())

    def cross(self, other):
        """Calculates and returns the cross product with another vector, facilitating vectorial computations in 3D space."""
        new_vector = self.vector.cross(other.to_xyz())
        return VectorAdapter(new_vector.xyz(), 'xyz')

    def length(self):
        """Returns the magnitude of the vector, providing insights into vector length in the current coordinate system."""
        return self.vector.length()

    def angle_with(self, other):
        """Calculates and returns the angle with another vector, aiding in the analysis of vector orientations."""
        return self.vector.angle(other.to_xyz())

    def spherical(self):
        """Returns the spherical coordinates of the vector, offering an alternative geometric perspective."""
        return self.vector.spherical()

    def quadray(self):
        """Returns the quadray (IVM) coordinates of the vector, enriching the geometric analysis toolkit."""
        return self.qvector.coords

    def __format__(self, format_spec):
        """Enables custom formatting for printing, showcasing the vector's representation according to the specified format."""
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
        print(f"| {test_vector['description']:30} | {initial_vector:20} | {converted_vector} |")

    # Calculating and displaying dot product and angle
    vec_ivm = VectorAdapter((1, 1, 1, 1), 'ivm')
    vec2_xyz = VectorAdapter((0.0, 1.0, 0.0), 'xyz')
    dot_product = vec_ivm.dot(vec2_xyz)
    angle = vec_ivm.angle_with(vec2_xyz)
    angle_display = f"{angle:.2f} degrees" if not math.isnan(angle) else "NaN"
    print(f"| {'Dot Product and Angle':30} | {'vec_ivm & vec2_xyz':20} | {dot_product}, {angle_display} |")

