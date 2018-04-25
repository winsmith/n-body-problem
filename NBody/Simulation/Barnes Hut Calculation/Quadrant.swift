//
//  Quadrant.swift
//  NBody
//
//  Created by Daniel Jilg on 25.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import Foundation

/// A Quadrant describes a square region in space.
///
/// In our two dimensional simulation, a quadrant has x and y
/// coordinates for its center, as well as a diameter property
/// that describes its width.
struct Quadrant {
    var center: Position
    var diameter: Double

    func contains(_ position: Position) -> Bool {
        return (
            position.x <= center.x + diameter/2 &&
            position.x >= center.x - diameter/2 &&
            position.y <= center.y + diameter/2 &&
            position.y >= center.y - diameter/2
        )
    }

    func subquadrantNorthWest() -> Quadrant {
        return Quadrant(
            center: Position(x: center.x - diameter/4, y: center.y + diameter/4),
            diameter: diameter/2
        )
    }

    func subquadrantNorthEast() -> Quadrant {
        return Quadrant(
            center: Position(x: center.x + diameter/4, y: center.y + diameter/4),
            diameter: diameter/2
        )
    }

    func subquadrantSouthWest() -> Quadrant {
        return Quadrant(
            center: Position(x: center.x - diameter/4, y: center.y - diameter/4),
            diameter: diameter/2
        )
    }

    func subquadrantSouthEast() -> Quadrant {
        return Quadrant(
            center: Position(x: center.x + diameter/4, y: center.y - diameter/4),
            diameter: diameter/2
        )
    }
}
