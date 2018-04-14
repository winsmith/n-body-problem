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

struct Position: Coordinate {
    var x: Double
    var y: Double

    /// Return the distance between two positions
    func distance(to otherPosition: Position) -> Double {
        let dx = self.x - otherPosition.x
        let dy = self.y - otherPosition.y
        return sqrt(dx * dx + dy * dy)
    }
}

struct Vector: Coordinate {
    var x: Double
    var y: Double
}
