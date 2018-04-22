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
    public let solarMass = 1.988435e30
    public let smallestPlanetMass = 3.30104e23
    public let largestPlanetMass = 1.89813e27
    public let radius = 1e12
    public let parentBodyColor = #colorLiteral(red: 0.9529411793, green: 0.6862745285, blue: 0.1333333403, alpha: 1)

    /// Initialize N bodies with random positions and circular-ish velocities
    init(numberOfBodies: Int) {
        // Put something heavy into the center
        let sun = Planetoid(
            position: Position(x: 0, y: 0),
            direction: Vector(x: 0, y: 0),
            name: "Sün",
            tickNumber: 0,
            mass: solarMass
        )
        sun.color = parentBodyColor
        self.bodies.append(sun)

        // Put some bodies around it
        for i in 1...numberOfBodies {
            let position = Position(x: (drand48() * 2 - 1) * radius, y: (drand48() * 2 - 1) * radius)
            let velocity = circularVelocity(for: position)
            let mass = smallestPlanetMass + ((largestPlanetMass - smallestPlanetMass) * drand48())
            bodies.append(Planetoid(position: position, direction: velocity, name: "Body \(i)", tickNumber: 0, mass: mass))
        }
    }

    func update(elapsedTime: Double) {
        fatalError("Not Implemented")
    }


    // MARK: Helper Methods
    /// Return the orbital velocity an orbiting body should have at a given position to stay in a perfect orbit
    public func circularVelocity(for position: Position) -> Vector {
        return Vector(x: 0, y: 0)

        let r2 = sqrt(position.x.squared + position.y.squared)
        let numerator = 6.67e-11 * solarMass
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
