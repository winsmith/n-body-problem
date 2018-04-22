//
//  Body.swift
//  NBody
//
//  Created by Daniel Jilg on 14.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import AppKit
import Foundation

/// Any object a universe keeps track of
class UniverseObject: CustomStringConvertible {
    var tickNumber: Int = 0
    var name: String
    lazy var color: NSColor = { return NSColor.random() }()

    init(tickNumber: Int, name: String) {
        self.tickNumber = tickNumber
        self.name = name
    }

    var description: String {
        return name
    }

    /// Update the UniverseObject between calculated frames
    func update(timeSteps: Double) {
    }
}

/// Any *physical* object a universe keeps track of
class Body: UniverseObject {
    /// The body's current position in the universe.
    var position: Position

    /// The body's travel direction and speed.
    /// Will be added to the body's position at the beginning of each step.
    var direction: Vector

    /// The sum of acting forces acting on this body.
    /// Will be applied to the direction vector at the end of each calculation step,
    var force: Vector

    init(position: Position, direction: Vector, name: String = "Unnamed Body", tickNumber: Int = 0) {
        self.position = position
        self.direction = direction
        self.force = Vector(x: 0, y: 0)

        super.init(tickNumber: tickNumber, name: name)
    }

    /// Set the sum of acting forces to zero
    func resetForce() {
        force = Vector(x: 0, y: 0)
    }

    func move(for timeSteps: Double) {
        position = position + direction * timeSteps
    }
}

/// A large physical object with considerable mass
class Planetoid: Body {
    var mass: Double

    init(position: Position, direction: Vector, name: String = "Unnamed Planetoid", tickNumber: Int = 0, mass: Double = 7.34767309e22) {
        self.mass = mass

        super.init(position: position, direction: direction, name: name, tickNumber: tickNumber)
    }


    /// Update the velocity and position
    // TODO: This should work with a body as well
    override func update(timeSteps: Double) {
        let timesForce = force * timeSteps
        let massAdjustedTimesForce = timesForce / mass
        direction = direction + massAdjustedTimesForce
        move(for: timeSteps)
    }

    /// Compute the net force acting between this body and otherBody and add to the net force acting on this body
    // TODO: This should work between a body and a planetoid as well
    func accelerate(with otherPlanetoid: Planetoid) {
        guard self !== otherPlanetoid else { return }
        guard otherPlanetoid.name == "Sün" else { return }

        // softening parameter (just to avoid infinities)
        let eps = 3E4

        let distance = position.distance(to: otherPlanetoid.position)
        let distanceX = otherPlanetoid.position.x - position.x
        let distanceY = otherPlanetoid.position.y - position.y
        let actingForce = (G * mass * otherPlanetoid.mass) / (distance.squared + eps.squared)

        force = Vector(
            x: direction.x + actingForce * distanceX / distance,
            y: direction.y + actingForce * distanceY / distance
        )
    }
}
