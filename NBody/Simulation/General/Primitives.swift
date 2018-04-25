//
//  Primitives.swift
//  NBody
//
//  Created by Daniel Jilg on 14.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import Foundation

protocol Coordinate {
    var x: Double { get }
    var y: Double { get }
}

struct Position: Coordinate, CustomStringConvertible {
    var description: String { return "x: \(x), y: \(y)" }

    var x: Double
    var y: Double

    /// Return the distance between two positions
    func distance(to otherPosition: Position) -> Double {
        let dx = self.x - otherPosition.x
        let dy = self.y - otherPosition.y
        return sqrt(dx.squared + dy.squared)
    }

    /// Add a Vector to a Position
    static func +(_ position: Position, _ vector: Vector) -> Position {
        return Position(
            x: position.x + vector.x,
            y: position.y + vector.y
        )
    }
}

struct Vector: Coordinate, CustomStringConvertible {
    var description: String { return "x: \(x), y: \(y)" }

    var x: Double
    var y: Double

    /// Add two Vectors
    static func +(_ lhs: Vector, _ rhs: Vector) -> Vector {
        return Vector(
            x: lhs.x + rhs.x,
            y: lhs.y + rhs.y
        )
    }

    /// Multiply a Vector by a Double
    static func *(_ lhs: Vector, _ rhs: Double) -> Vector {
        return Vector(
            x: lhs.x * rhs,
            y: lhs.y * rhs
        )
    }

    /// Divide a Vector by a Double
    static func /(_ lhs: Vector, _ rhs: Double) -> Vector {
        return Vector(
            x: lhs.x / rhs,
            y: lhs.y / rhs
        )
    }

}
