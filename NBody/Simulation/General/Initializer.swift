//
//  Initializer.swift
//  NBody
//
//  Created by Daniel Jilg on 27.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import AppKit
import Foundation

protocol UniverseInitializer {
    func createBodies(radius: Double) -> [Body]
}

/// Initialize N bodies with random positions and circular-ish velocities around a sun-like object
struct RandomSolarInitializer: UniverseInitializer {
    let numberOfBodies: Int
    public let parentBodyColor = #colorLiteral(red: 0.9529411793, green: 0.6862745285, blue: 0.1333333403, alpha: 1)
    public let solarMass = 1.988435e30
    public let smallestPlanetMass = 3.30104e23
    public let largestPlanetMass = 1.89813e27

    func createBodies(radius: Double) -> [Body] {
        var bodies = [Body]()

        // Put something heavy into the center
        let sun = Planetoid(
            position: Position(x: 0, y: 0),
            direction: Vector(x: 0, y: 0),
            name: "Sün",
            tickNumber: 0,
            mass: solarMass,
            radius: 6.9e8
        )
        sun.color = parentBodyColor
        bodies.append(sun)

        // Put some bodies around it
        for _ in 1...numberOfBodies {
            let freeSpace = 0.5 * radius

            var position = Position(x: 0, y: 0)
            repeat {
                let positionX = (drand48() * radius * 2) - radius
                let positionY = (drand48() * radius * 2) - radius
                position = Position(x: positionX , y: positionY)
            } while position.distance(to: sun.position) < freeSpace

            let velocity = circularVelocity(for: position)
            let mass = smallestPlanetMass + ((largestPlanetMass - smallestPlanetMass) * drand48())
            bodies.append(Planetoid(position: position, direction: velocity, name: nil, tickNumber: 0, mass: mass))
        }

        return bodies
    }

    /// Return the orbital velocity an orbiting body should have at a given position to stay in a stable orbit
    ///
    /// This function ignores the orbiting body's mass, so it's not very accurate for high-mass bodies
    /// But that's ok since we don't want perfect boring orbits anyway.
    public func circularVelocity(for position: Position) -> Vector {
        // Calculate orbital velocity
        let standardGravitationalParameter = G * solarMass
        let orbitalRadius = position.distance(to: Position(x: 0, y: 0))
        var orbitalVelocity = sqrt(standardGravitationalParameter / orbitalRadius)

        // Reverse velocity for a small percentage of bodies
        if drand48() < 0.9 {
            orbitalVelocity = -orbitalVelocity
        }

        // calculate angle at given position
        let absoluteAngle = atan(abs(position.y / position.x))
        let thetaV = Double.pi / 2 - absoluteAngle

        // calculate velocity vector at given angle
        let vectorX = (position.y > 0 ? -1 : 1) * cos(thetaV) * orbitalVelocity
        let vectorY = (position.x > 0 ? 1 : -1) * sin(thetaV) * orbitalVelocity
        return Vector(x: vectorX, y: vectorY)
    }
}
