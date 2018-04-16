//
//  Universe.swift
//  NBody
//
//  Created by Daniel Jilg on 14.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import Foundation

/// A container for simulation of orbital dynamics
class Universe {
    // MARK: Properties
    public private(set) var bodies = [Body]()
    public let solarMass = 1.98892e30

    // MARK: Helper Methods
    /// Return the orbital velocity an orbiting body should have at a given position to stay in a perfect orbit
    public func circularVelocity(for position: Position) -> Vector {
        let r2 = sqrt(position.x.squared + position.y.squared)
        let numerator = 6.67e-11 * 1e6 * solarMass
        let circularVelocity = sqrt(numerator/r2)

        // TODO
        //        vx = -1 * copysign(1, py) * cos(thetav) * magv
        //        vy = copysign(1, px) * sin(thetav) * magv

        return Vector(x: circularVelocity, y: 0)
    }
}
