// swift-tools-version: 5.9

import PackageDescription

let package = Package(
    name: "ActiveInferenceSwift",
    platforms: [
        .macOS(.v13),
        .iOS(.v16),
        .tvOS(.v16),
        .watchOS(.v9),
        .visionOS(.v1)
    ],
    products: [
        .executable(
            name: "ActiveInferenceSwift",
            targets: ["ActiveInferenceSwift"]
        ),
        .library(
            name: "ActiveInference",
            targets: ["ActiveInference"]
        )
    ],
    targets: [
        .executableTarget(
            name: "ActiveInferenceSwift",
            dependencies: ["ActiveInference"]
        ),
        .target(
            name: "ActiveInference",
            dependencies: []
        ),
        .testTarget(
            name: "ActiveInferenceTests",
            dependencies: ["ActiveInference"]
        )
    ]
)
