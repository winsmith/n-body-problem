//
//  Universe.swift
//  NBody
//
//  Created by Daniel Jilg on 14.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import AppKit
import Foundation

/// A container for simulation of orbital dynamics
class Universe {
    // MARK: Properties
    public private(set) var bodies = [Body]()

    // MARK: - Configuration
    public let solarMass = 1.98892e30
    public let radius = 1e18
    public let parentBodyColor = #colorLiteral(red: 0.9529411793, green: 0.6862745285, blue: 0.1333333403, alpha: 1)

    /// Initialize N bodies with random positions and circular-ish velocities
    init(numberOfBodies: Int) {
        // Put something heavy into the center
        let sun = Planetoid(
            position: Position(x: 0, y: 0),
            direction: Vector(x: 0, y: 0),
            name: "Sün",
            tickNumber: 0,
            mass: solarMass * 1e6
        )
        sun.color = parentBodyColor
        self.bodies.append(sun)

        // Put some bodies around it
        for i in 1...numberOfBodies {
            let position = Position(x: (radius + 1e8) * exp(-1.8) * (0.5-drand48()), y: (radius + 1e8) * exp(-1.8) * (0.5-drand48()))
            let velocity = circularVelocity(for: position)
            let mass = drand48() * solarMass * 30 + 1e20
            bodies.append(Planetoid(position: position, direction: velocity, name: "Body \(i)", tickNumber: 0, mass: mass))
        }
    }

    func update(elapsedTime: Double) {
        fatalError("Not Implemented")
    }


    // MARK: Helper Methods
    /// Return the orbital velocity an orbiting body should have at a given position to stay in a perfect orbit
    public func circularVelocity(for position: Position) -> Vector {
        let r2 = sqrt(position.x.squared + position.y.squared)
        let numerator = 6.67e-11 * 1e6 * solarMass
        let circularVelocity = sqrt(numerator/r2)
        let randomizedVelocity = circularVelocity * (0.7 + drand48() * 0.5)
        let absangle = atan(abs(position.y / position.x))
        let thetav = Double.pi / 2 - absangle

        let vx = -1 * Double(position.y.sign.rawValue) * cos(thetav) * randomizedVelocity
        let vy = Double(position.x.sign.rawValue) * sin(thetav) * randomizedVelocity

        return Vector(x: vx, y: vy)
    }
}

class BruteForceUniverse: Universe {
    override func update(elapsedTime: Double) {
        for body in bodies where body is Planetoid {
            body.resetForce()

            // uh, oh a loop inside a loop
            // This'll get us n^2 complexity
            for otherBody in bodies where body is Planetoid {
                if otherBody !== body {
                    (body as! Planetoid).accelerate(with: (otherBody as! Planetoid))
                }
            }
        }

        for body in bodies {
            body.update(timeSteps: elapsedTime)
        }
    }
}
