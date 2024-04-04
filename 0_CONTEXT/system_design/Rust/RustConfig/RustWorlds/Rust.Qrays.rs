# https://github.com/4dsolutions/m4w/blob/main/qrays.py
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
    a: f64,
    a2: f64,
    b: f64, 
    b2: f64,
    c: f64,
    c2: f64,
    d: f64,
    d2: f64,
    e: f64,
    e2: f64,
    f: f64,
    f2: f64,
    ab: f64,
    ac: f64,
    ad: f64,
    bc: f64,
    cd: f64,
    db: f64,
    bac: f64,
    cad: f64,
    bad: f64,
    abc: f64,
    cbd: f64,
    abd: f64,
    acb: f64,
    acd: f64,
    bcd: f64,
    adc: f64,
    bdc: f64,
    adb: f64,
}

impl Tetrahedron {
    fn new(a: f64, b: f64, c: f64, d: f64, e: f64, f: f64) -> Self {
        let a2 = a.powi(2);
        let b2 = b.powi(2);
        let c2 = c.powi(2);
        let d2 = d.powi(2);
        let e2 = e.powi(2);
        let f2 = f.powi(2);

        let bac = ((a2 + b2 - d2) / (2.0 * a * b)).acos();
        let cad = ((b2 + c2 - e2) / (2.0 * b * c)).acos();
        let bad = ((a2 + c2 - f2) / (2.0 * a * c)).acos();

        let abc = ((a2 + d2 - b2) / (2.0 * a * d)).acos();
        let cbd = ((d2 + f2 - e2) / (2.0 * d * f)).acos();
        let abd = ((a2 + f2 - c2) / (2.0 * a * f)).acos();

        let acb = ((b2 + d2 - a2) / (2.0 * b * d)).acos();
        let acd = ((b2 + e2 - c2) / (2.0 * b * e)).acos();
        let bcd = ((d2 + e2 - f2) / (2.0 * d * e)).acos();

        let adc = ((c2 + e2 - b2) / (2.0 * c * e)).acos();
        let bdc = ((e2 + f2 - d2) / (2.0 * e * f)).acos();
        let adb = ((c2 + f2 - a2) / (2.0 * c * f)).acos();

        Self {
            a,
            a2,
            b,
            b2,
            c,
            c2,
            d,
            d2,
            e,
            e2,
            f,
            f2,
            ab: a,
            ac: b,
            ad: c,
            bc: d,
            cd: e,
            db: f,
            bac,
            cad,
            bad,
            abc,
            cbd,
            abd,
            acb,
            acd,
            bcd,
            adc,
            bdc,
            adb,
        }
    }

    fn dump(&self) -> (f64, f64, f64) {
        (self.a2, self.b2, self.c2)
    }

    fn mul(&self, other: f64) -> Self {
        let a = self.a * other;
        let b = self.b * other;
        let c = self.c * other;
        let d = self.d * other;
        let e = self.e * other;
        let f = self.f * other;
        Self::new(a, b, c, d, e, f)
    }

    fn edges(&self) -> std::collections::HashMap<&str, f64> {
        std::collections::HashMap::from([
            ("AB", self.a),
            ("AC", self.b),
            ("AD", self.c),
            ("BC", self.d),
            ("DC", self.e),
            ("BD", self.f),
        ])
    }

    fn angles(&self, values: bool, prec: usize) -> std::collections::HashMap<&str, f64> {
        if values {
            std::collections::HashMap::from([
                ("BAC", self.bac.to_degrees()),
                ("CAD", self.cad.to_degrees()),
                ("BAD", self.bad.to_degrees()),
                ("ABC", self.abc.to_degrees()),
                ("CBD", self.cbd.to_degrees()),
                ("ABD", self.abd.to_degrees()),
                ("ACB", self.acb.to_degrees()),
                ("ACD", self.acd.to_degrees()),
                ("BCD", self.bcd.to_degrees()),
                ("ADC", self.adc.to_degrees()),
                ("BDC", self.bdc.to_degrees()),
                ("ADB", self.adb.to_degrees()),
            ])
        } else {
            std::collections::HashMap::from([
                ("BAC", self.bac),
                ("CAD", self.cad),
                ("BAD", self.bad),
                ("ABC", self.abc),
                ("CBD", self.cbd),
                ("ABD", self.abd),
                ("ACB", self.acb),
                ("ACD", self.acd),
                ("BCD", self.bcd),
                ("ADC", self.adc),
                ("BDC", self.bdc),
                ("ADB", self.adb),
            ])
        }
    }

    fn degrees(&self, values: bool, prec: usize) -> std::collections::HashMap<&str, f64> {
        let mut output = std::collections::HashMap::new();
        if values {
            for (k, v) in self.angles(true, prec) {
                output.insert(k, v.to_degrees());
            }
        } else {
            for (k, v) in self.angles(false, prec) {
                output.insert(k, v.to_degrees());
            }
        }
        output
    }

    fn ivm_volume(&self, value: bool, prec: usize) -> f64 {
        let ivmvol = pdf(self.a, self.b, self.c, self.d, self.e, self.f);
        if value {
            ivmvol
        } else {
            ivmvol.round_prec(prec)
        }
    }

    fn xyz_volume(&self, value: bool, prec: usize) -> f64 {
        let xyzvol = (1.0 / SYN3) * self.ivm_volume(value, prec);
        if value {
            xyzvol
        } else {
            xyzvol.round_prec(prec)
        }
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
    Tetrahedron::new(
        v0.norm(),
        v1.norm(),
        v2.norm(),
        (v0 - v1).norm(),
        (v1 - v2).norm(),
        (v2 - v0).norm(),
    )
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

struct B;

impl Tetrahedron for B {
    fn new() -> Self {
        let bmod_ea = ROOT2 / 2.0;
        let bmod_eb = ROOT6 / 12.0;
        let bmod_ec = 0.5;
        let bmod_ab = ROOT6 / 4.0;
        let bmod_bc = ROOT2 / 4.0;
        let bmod_ac = 0.5;
        Self::new(bmod_ea, bmod_eb, bmod_ec, bmod_ab, bmod_bc, bmod_ac)
    }
}

struct E;

impl Tetrahedron for E {
    fn new() -> Self {
        let e0 = D / 2.0;
        let e1 = ROOT3 * PHI.powi(-1) / 2.0;
        let e2 = ((5.0 - ROOT5) / 2.0).sqrt() / 2.0;
        let e3 = (3.0 - ROOT5) / 2.0 / 2.0;
        let e4 = (5.0 - 2.0 * ROOT5).sqrt() / 2.0;
        let e5 = 1.0 / PHI / 2.0;
        Self::new(e0, e1, e2, e3, e4, e5)
    }
}

struct A;

impl Tetrahedron for A {
    fn new() -> Self {
        let one = Vector4::new(1.0,


