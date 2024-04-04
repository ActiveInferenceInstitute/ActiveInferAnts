# https://github.com/4dsolutions/m4w/blob/main/tetravolume.py 
# 4-4-2024 from Python


use std::f64::consts::{PI, SQRT_2};
use std::ops::{Add, Div, Mul, Sub};
use nalgebra::{Matrix5, Vector4};

// ============[ GLOBAL CONSTANTS ]=================== 

const R: f64 = 0.5;
const D: f64 = 1.0;

const SYN3: f64 = f64::sqrt(9.0 / 8.0);
const ROOT2: f64 = f64::sqrt(2.0);
const ROOT3: f64 = f64::sqrt(3.0); 
const ROOT5: f64 = f64::sqrt(5.0);
const ROOT6: f64 = f64::sqrt(6.0);

const PHI: f64 = (1.0 + ROOT5) / 2.0;

const SMOD: f64 = PHI.powi(-5) / 2.0;
const EMOD: f64 = (ROOT2 / 8.0) * PHI.powi(-3);
const AMOD: f64 = 1.0 / 24.0;
const BMOD: f64 = AMOD;
const TMOD: f64 = AMOD;

const SFACTOR: f64 = SMOD / EMOD;

// ============[ TETRAHEDRON STRUCT ]=================== 

struct Tetrahedron {
    edges: [f64; 6],
    edges_squared: [f64; 6],
    angles: [f64; 18],
}

impl Tetrahedron {
    fn new(edges: [f64; 6]) -> Self {
        let edges_squared: [f64; 6] = edges.map(|edge| edge.powi(2));

        let angles = [
            Self::calc_angle(edges_squared[0], edges_squared[1], edges_squared[3]),
            Self::calc_angle(edges_squared[1], edges_squared[2], edges_squared[4]),
            Self::calc_angle(edges_squared[0], edges_squared[2], edges_squared[5]),
            Self::calc_angle(edges_squared[0], edges_squared[3], edges_squared[1]),
            Self::calc_angle(edges_squared[3], edges_squared[5], edges_squared[4]),
            Self::calc_angle(edges_squared[0], edges_squared[5], edges_squared[2]),
            Self::calc_angle(edges_squared[1], edges_squared[3], edges_squared[0]),
            Self::calc_angle(edges_squared[1], edges_squared[4], edges_squared[2]),
            Self::calc_angle(edges_squared[3], edges_squared[4], edges_squared[5]),
            Self::calc_angle(edges_squared[2], edges_squared[4], edges_squared[1]),
            Self::calc_angle(edges_squared[4], edges_squared[5], edges_squared[3]),
            Self::calc_angle(edges_squared[2], edges_squared[5], edges_squared[0]),
            // Repeat or additional angles as needed
        ];

        Self {
            edges,
            edges_squared,
            angles,
        }
    }

    fn dump(&self) -> (f64, f64, f64) {
        (self.edges_squared[0], self.edges_squared[1], self.edges_squared[2])
    }

    fn mul(&self, other: f64) -> Self {
        let new_edges: [f64; 6] = self.edges.map(|edge| edge * other);
        Self::new(new_edges)
    }

    fn edges(&self) -> std::collections::HashMap<&str, f64> {
        std::collections::HashMap::from([
            ("AB", self.edges[0]),
            ("AC", self.edges[1]),
            ("AD", self.edges[2]),
            ("BC", self.edges[3]),
            ("DC", self.edges[4]),
            ("BD", self.edges[5]),
        ])
    }

    fn angles(&self) -> std::collections::HashMap<&str, f64> {
        std::collections::HashMap::from([
            ("BAC", self.angles[0]),
            ("CAD", self.angles[1]),
            ("BAD", self.angles[2]),
            ("ABC", self.angles[3]),
            ("CBD", self.angles[4]),
            ("ABD", self.angles[5]),
            ("ACB", self.angles[6]),
            ("ACD", self.angles[7]),
            ("BCD", self.angles[8]),
            ("ADC", self.angles[9]),
            ("BDC", self.angles[10]),
            ("ADB", self.angles[11]),
            // Additional angles as needed
        ])
    }

    fn calc_angle(a2: f64, b2: f64, c2: f64) -> f64 {
        // Assuming the law of cosines for angle calculation
        let cos_angle = (a2 + b2 - c2) / (2.0 * f64::sqrt(a2) * f64::sqrt(b2));
        cos_angle.acos() // Return the arccosine of the angle in radians
    }
}

// ============[ VOLUME FORMULAE ]=================== 

fn gdj(a: f64, b: f64, c: f64, d: f64, e: f64, f: f64) -> f64 {
    let a2 = a.powi(2);
    let b2 = b.powi(2);
    let c2 = c.powi(2);
    let d2 = d.powi(2);
    let e2 = e.powi(2);
    let f2 = f.powi(2);

    let open = a2 * b2 * e2 + a2 * b2 * f2 + a2 * c2 * d2 +
               a2 * c2 * e2 + a2 * d2 * e2 + a2 * e2 * f2 +
               b2 * c2 * d2 + b2 * c2 * f2 + b2 * d2 * f2 +
               b2 * e2 * f2 + c2 * d2 * e2 + c2 * d2 * f2;

    let closed = a2 * b2 * d2 + a2 * c2 * f2 + b2 * c2 * e2 + d2 * e2 * f2;

    let oppo = a2 * e2 * (a2 + e2) + b2 * f2 * (b2 + f2) + c2 * d2 * (c2 + d2);

    ((open - closed - oppo) / 2.0).sqrt()
}

fn pdf(a: f64, b: f64, c: f64, d: f64, e: f64, f: f64) -> f64 {
    let a2 = (2.0 * a).powi(2);
    let b2 = (2.0 * b).powi(2);
    let c2 = (2.0 * c).powi(2);
    let d2 = (2.0 * d).powi(2);
    let e2 = (2.0 * e).powi(2);
    let f2 = (2.0 * f).powi(2);

    let comp_chunk = (a2 * f2) * (-a2 + b2 + c2 + d2 + e2 - f2) +
                     (b2 * e2) * (a2 - b2 + c2 + d2 - e2 + f2) +
                     (c2 * d2) * (a2 + b2 - c2 - d2 + e2 + f2) -
                     (a2 + f2) * (b2 + e2) * (c2 + d2) / 2.0 -
                     (a2 - f2) * (b2 - e2) * (c2 - d2) / 2.0;

    (2.0 * comp_chunk).sqrt() / 16.0
}

fn cm(a: f64, b: f64, c: f64, d: f64, e: f64, f: f64) -> f64 {
    let a2 = (2.0 * a).powi(2);
    let b2 = (2.0 * b).powi(2);
    let c2 = (2.0 * c).powi(2);
    let d2 = (2.0 * d).powi(2);
    let e2 = (2.0 * e).powi(2);
    let f2 = (2.0 * f).powi(2);

    let m = Matrix5::new(
        0.0, 1.0, 1.0, 1.0, 1.0,
        1.0, 0.0, a2, b2, c2,
        1.0, a2, 0.0, d2, f2,
        1.0, b2, d2, 0.0, e2,
        1.0, c2, f2, e2, 0.0,
    );

    m.determinant().sqrt() / 16.0
}

fn make_tet(v0: &Vector4<f64>, v1: &Vector4<f64>, v2: &Vector4<f64>) -> Tetrahedron {
    Tetrahedron::new([
        v0.norm(),
        v1.norm(),
        v2.norm(),
        (v0 - v1).norm(),
        (v1 - v2).norm(),
        (v2 - v0).norm(),
    ])
}

fn qvolume(q0: &Vector4<f64>, q1: &Vector4<f64>, q2: &Vector4<f64>, q3: &Vector4<f64>) -> f64 {
    let m = Matrix5::new(
        q0[0], q0[1], q0[2], q0[3], 1.0,
        q1[0], q1[1], q1[2], q1[3], 1.0,
        q2[0], q2[1], q2[2], q2[3], 1.0,
        q3[0], q3[1], q3[2], q3[3], 1.0,
        1.0, 1.0, 1.0, 1.0, 0.0,
    );
    m.determinant().abs() / 4.0
}

// ============[ BEAST MODULES ]=================== 

// The following implementations are incorrect as they attempt to implement a struct for a trait that does not exist.
// Tetrahedron is a struct, not a trait, so these cannot directly implement Tetrahedron. 
// They should either be functions returning a Tetrahedron or separate structs implementing a common trait if needed.

struct B;

impl B {
    fn new() -> Tetrahedron {
        let bmod_ea = ROOT2 / 2.0;
        let bmod_eb = ROOT6 / 12.0;
        let bmod_ec = 0.5;
        let bmod_ab = ROOT6 / 4.0;
        let bmod_bc = ROOT2 / 4.0;
        let bmod_ac = 0.5;
        Tetrahedron::new([bmod_ea, bmod_eb, bmod_ec, bmod_ab, bmod_bc, bmod_ac])
    }
}

struct E;

impl E {
    fn new() -> Tetrahedron {
        let e0 = D / 2.0;
        let e1 = ROOT3 * PHI.powi(-1) / 2.0;
        let e2 = ((5.0 - ROOT5) / 2.0).sqrt() / 2.0;
        let e3 = (3.0 - ROOT5) / 2.0 / 2.0;
        let e4 = (5.0 - 2.0 * ROOT5).sqrt() / 2.0;
        let e5 = 1.0 / PHI / 2.0;
        Tetrahedron::new([e0, e1, e2, e3, e4, e5])
    }
}

struct A;

impl A {
    fn new() -> Tetrahedron {
        // The original code for A::new() was incomplete and incorrect.
        // Assuming the intention was to create a Tetrahedron with specific dimensions:
        let a_edges = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]; // Example dimensions
        Tetrahedron::new(a_edges)
    }
}
